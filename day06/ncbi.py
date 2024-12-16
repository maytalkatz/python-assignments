import requests
import csv
import os
import time
from datetime import datetime
from Bio import Entrez
import argparse
import sys
from urllib.error import HTTPError

def parse_arguments():
    if len(sys.argv) == 2 and sys.argv[1].startswith('-'):
        sys.argv = ['ncbi.py', '--term', sys.argv[1][1:]]  

    parser = argparse.ArgumentParser(description='Download data from NCBI')
    parser.add_argument('--database', default='nucleotide', help='Database to search (default: nucleotide)')
    parser.add_argument('--term', help='Search term', required=True)
    parser.add_argument('--number', type=int, default=10, help='Number of items to download (default: 10)')
    args = parser.parse_args()
    return args

def search_ncbi(database, term, number):
    Entrez.email = "maytal.katz@weizmann.ac.il"  
    print(f"Searching NCBI database '{database}' for term '{term}'...")
    try:
        handle = Entrez.esearch(db=database, term=term, retmax=number)
        record = Entrez.read(handle)
        total = record["Count"]
        print(f"Found {total} records. Downloading up to {number} items...")
        return record, total
    except Exception as e:
        print(f"Error during search: {e}")
        exit()

def get_rettype_and_retmode(database):
    if database.lower() == 'nucleotide':
        return "gb", "text"
    elif database.lower() == 'genome':
        return "docsum", "xml"  
    elif database.lower() == 'protein':
        return "fasta", "text"
    else:
        return "gb", "text"  

def download_data(record, database, term, number):
    os.makedirs(term, exist_ok=True)  
    rettype, retmode = get_rettype_and_retmode(database)

    file_names = []
    for i, id in enumerate(record['IdList']):
        try:
            time.sleep(1)  
            fetch_handle = Entrez.efetch(db=database, id=id, rettype=rettype, retmode=retmode)
            data = fetch_handle.read()

            if isinstance(data, bytes):
                data = data.decode('utf-8')

            file_name = f"{term}/{term}_{i+1}.txt"
            with open(file_name, 'w') as f:
                f.write(data)
            file_names.append(file_name)
            print(f"Saved: {file_name}")
        except HTTPError as e:
            print(f"Failed to fetch data for ID {id}: {e}")
        except Exception as e:
            print(f"Error: {e}")

    return file_names

def save_metadata(database, term, number, total):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile('metadata.csv')

    with open('metadata.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:  
            writer.writerow(['date', 'database', 'term', 'max', 'total'])
        writer.writerow([date, database, term, number, total])

    print("\nMetadata:")
    print(f"date,database,term,max,total")
    print(f"{date},{database},{term},{number},{total}")

def main():
    args = parse_arguments()
    record, total = search_ncbi(args.database, args.term, args.number)
    file_names = download_data(record, args.database, args.term, args.number)

    if file_names:
        print("\nDownloaded files:")
        for file in file_names:
            print(f"- {file}")
    else:
        print("\nNo files were downloaded.")

    save_metadata(args.database, args.term, args.number, total)

if __name__ == '__main__':
    main()
