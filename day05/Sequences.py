import sys
from collections import Counter

# Process data
def process_sequence_file(filename):
    with open(filename, 'r') as file:
        sequence = file.read().strip()

    counts = Counter(sequence)
    total = sum(counts.values())

    percentages = {char: (count / total * 100) for char, count in counts.items()}
    stats = {char: (counts[char], percentages.get(char, 0)) for char in "ACGT"}
    
    unknown_count = total - sum(counts[char] for char in "ACGT")
    stats["Unknown"] = (unknown_count, unknown_count / total * 100 if total > 0 else 0)

    return stats, total

def print_stats(stats, total, label):
    print(f"{label}")
    for char in "ACGT":
        count, percent = stats.get(char, (0, 0))
        print(f"{char}: {count:8} {percent:5.1f}%")
    unknown_count, unknown_percent = stats.get("Unknown", (0, 0))
    print(f"Unknown: {unknown_count:8} {unknown_percent:5.1f}%")
    print(f"Total: {total:8}\n")


# Execute program:
def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <file1> <file2> ...")
        sys.exit(1)

    all_stats = Counter()
    all_total = 0

    for filename in sys.argv[1:]:
        stats, total = process_sequence_file(filename)
        print_stats(stats, total, label=filename)
        for char in stats:
            all_stats[char] += stats[char][0]  
        all_total += total

    combined_stats = {char: (all_stats[char], all_stats[char] / all_total * 100) for char in all_stats}
    print_stats(combined_stats, all_total, label="All")

if __name__ == "__main__":
    main()
