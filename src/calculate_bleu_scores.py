#!/usr/bin/env python
# coding: utf-8

"""
BLEU Score Pairwise Calculation Script
--------------------------------------
This script calculates BLEU scores for pairwise comparisons of processed text 
descriptions. It ensures that only samples belonging to **different GSEs** are compared.

Inputs:
    - A TSV file containing the following columns:
        1. Processed_Description (preprocessed text)
        2. GSM (sample ID)
        3. GSE (experiment ID)

Outputs:
    - A compressed CSV file containing the BLEU scores for valid sample pairs.

Requirements:
    - pandas
    - nltk
"""

import pandas as pd
from itertools import combinations
from nltk.translate.bleu_score import sentence_bleu

# Path to the processed data file
file_path = '/path/to/src/processed_txt2onto_descriptions_stem-False_lemmatize-False.tsv'

# Load the processed data
df = pd.read_csv(file_path, sep='\t')
df.columns = ['Processed_Description', 'GSM', 'GSE']  # Rename columns for clarity

# Function to calculate the BLEU score for a pair of rows
def calculate_bleu_pair(row1, row2):
    """
    Calculate BLEU score between two text descriptions.

    Args:
        row1 : First row containing 'Processed_Description' and GSM.
        row2 : Second row containing 'Processed_Description' and GSM.

    Returns:
        dict: Dictionary with GSM identifiers and BLEU score.
    """
    reference = row1['Processed_Description'].split()
    candidate = row2['Processed_Description'].split()
    bleu = sentence_bleu([reference], candidate)
    return {
        'GSM1': row1['GSM'],
        'GSM2': row2['GSM'],
        'BLEU': bleu
    }

# List to store BLEU scores for valid pairs
bleu_scores = []

# Iterate over all unique combinations of rows
for (i, row1), (j, row2) in combinations(df.iterrows(), 2):
    # Only calculate BLEU for pairs belonging to different GSEs
    if row1['GSE'] != row2['GSE']:
        score = calculate_bleu_pair(row1, row2)
        bleu_scores.append(score)

# Convert the list of BLEU scores to a DataFrame
bleu_scores_df = pd.DataFrame(bleu_scores)

# Output file path
output_file = '/path/to/results/tifours/bleu_scores_opt.csv.gz'

# Save the BLEU scores DataFrame to a compressed CSV file
bleu_scores_df.to_csv(output_file, index=False, compression='gzip')

# Print completion message
print(f"BLEU scores have been saved to {output_file}")