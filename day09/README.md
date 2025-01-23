# Sequence Analysis

This Python program is designed to analyze DNA sequences in FASTA format. It can find the longest contiguous repeating substring in the sequence, calculate the AT-CG ratio, and determine the melting temperature (Tm) of the sequence. The melting temperature is particularly useful for applications like PCR, DNA sequencing, DNA-protein interactions, and other molecular biology techniques.

## Features

- **Find the Longest Repeating Substring**: Identifies the longest contiguous repetition within the DNA sequence.
- **Calculate AT-CG Ratio**: Computes the ratio of adenine-thymine (AT) pairs to cytosine-guanine (CG) pairs in the sequence.
- **Melting Temperature (Tm)**: Calculates the melting temperature of the DNA sequence, which is critical for PCR and other biochemical applications.


## Usage
This program accepts input in the form of either a path to a FASTA file or the file name, provided your terminal is set to the appropriate directory.

### Analysis Options:
- `--duplicate` - Finds the longest repeating substring in the sequence.
- `--atcg_ratio` - Calculates and displays the AT-CG ratio and melting temperature (Tm) of the sequence.

### Run the script from the command line with the following syntax:
If using a path:

```bash
# If using a path:
python sequence_analysis.py "C:\\path\\to\\your\\directory\\example.fasta" --duplicate --atcg_ratio

#If using a file name:
python sequence_analysis.py example.fasta --duplicate --atcg_ratio

