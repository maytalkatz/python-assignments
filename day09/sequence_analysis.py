import argparse
import os

# Function to find the longest contiguous repeating substring
def find_longest_repeating_substring(sequence):
    n = len(sequence)
    longest_substring = ""

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = sequence[i:j]

            if sequence.count(substring) > 1 and len(substring) > len(longest_substring):
                longest_substring = substring

    return longest_substring

# Function to calculate AT-CG ratio and the melting temperature
def calculate_at_cg_ratio_and_tm(sequence):
    at_count = sequence.count('A') + sequence.count('T')
    cg_count = sequence.count('C') + sequence.count('G')
    total_count = len(sequence)

    # AT/CG ratio
    if cg_count > 0:  
        at_cg_ratio = at_count / cg_count
    else:
        at_cg_ratio = float('inf')  

    # Melting temperature
    if total_count < 14:
        tm = (at_count * 2) + (cg_count * 4)
    else:
        tm = 64.9 + 41 * ((cg_count - 16.4) / total_count)

    return at_cg_ratio, tm

# Function to parse a FASTA file
def parse_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    sequence = ""
    for line in lines:
        if not line.startswith(">"):  
            sequence += line.strip() 
    return sequence

# Main function
def main():
    parser = argparse.ArgumentParser(description="Analyze DNA sequences.")
    parser.add_argument("path", help="Path to the input file (FASTA format) or file name if in the current directory")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest repeating substring")
    parser.add_argument("--atcg_ratio", action="store_true", help="Calculate AT-CG ratio and melting temperature")
    args = parser.parse_args()

    # Resolve file path: 
    if os.path.isfile(args.path):
        file_path = args.path
    elif os.path.isfile(os.path.join(os.getcwd(), args.path)):
        file_path = os.path.join(os.getcwd(), args.path)
    else:
        print(f"Error: File '{args.path}' not found.")
        return

    # Parse the sequence from the input file
    try:
        sequence = parse_fasta(file_path)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if args.duplicate:
        longest_repeat = find_longest_repeating_substring(sequence)
        print(f"Longest Repeating Substring: {longest_repeat}")

    if args.atcg_ratio:
        at_cg_ratio, tm = calculate_at_cg_ratio_and_tm(sequence)
        print(f"AT-CG Ratio: {at_cg_ratio:.2f}")
        print(f"Melting Temperature: {tm:.2f}°C")

if __name__ == "__main__":
    main()
