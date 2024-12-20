#!/usr/bin/env python
# coding: utf-8

"""
filter_bleu_scores_by_tissue_array.py
--------------------------------------

Description:
This script filters BLEU scores based on ground truth tissue labels for use in a job array. 

It categorizes valid sample pairs according to specific conditions:
    - Matching pairs (1,1): Both samples belong to the tissue.
    - Mixed pairs (-1,1) or (1,-1): One sample belongs to the tissue, the other does not.

Inputs:
- Tissue label file: CSV file containing sample IDs and their tissue-specific labels.
- BLEU scores file: Precomputed BLEU scores for all sample pairs.
- Task file: File specifying the subset of tissue labels to process (used in job arrays).

Outputs:
- Filtered BLEU scores with assigned categories saved in the specified output directory.

"""

import argparse
import os
import pandas as pd
import sys

def parse_args():
    """
    Parse command-line arguments for the script.
    """
    parser = argparse.ArgumentParser(description="Filter BLEU scores by tissue labels for job arrays.")
    parser.add_argument("--tissue_labels", type=str, required=True,
                        help="Path to tissue label file (CSV).")
    parser.add_argument("--bleu_scores", type=str, required=True,
                        help="Path to precomputed BLEU scores file.")
    parser.add_argument("--output_dir", type=str, required=True,
                        help="Directory where results will be saved.")
    parser.add_argument("--task_file", type=str, required=True,
                        help="Path to task file specifying tissue labels to process.")
    return parser.parse_args()

def main():
    """
    Main function to filter BLEU scores for a specific task.
    """
    # Parse arguments
    args = parse_args()
    tissue_file = args.tissue_labels
    bleu_scores_file = args.bleu_scores
    output_dir = args.output_dir
    task_file = args.task_file

    # Load task-specific tissue labels
    with open(task_file, 'r') as f:
        tissue_files = [line.strip() for line in f]

    for tissue_file in tissue_files:
        # Load tissue labels
        tissue_labels_df = pd.read_csv(tissue_file)
        tissue_name = os.path.basename(tissue_file).replace('tissue_labels_', '').replace('.csv', '')

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Load BLEU scores
        bleu_scores_df = pd.read_csv(bleu_scores_file)

        # Map labels to BLEU pairs
        labels_dict = pd.Series(tissue_labels_df.iloc[:, 1].values, index=tissue_labels_df['Unnamed: 0']).to_dict()
        bleu_scores_df['Label1'] = bleu_scores_df['GSM1'].map(labels_dict)
        bleu_scores_df['Label2'] = bleu_scores_df['GSM2'].map(labels_dict)

        # Filter valid pairs
        valid_pairs = bleu_scores_df[
            ((bleu_scores_df['Label1'] == 1) & (bleu_scores_df['Label2'] == 1)) |
            ((bleu_scores_df['Label1'] == -1) & (bleu_scores_df['Label2'] == 1)) |
            ((bleu_scores_df['Label1'] == 1) & (bleu_scores_df['Label2'] == -1))
        ]

        if valid_pairs.empty:
            print(f"No valid pairs found for {tissue_name}. Skipping.")
            continue

        # Assign categories
        valid_pairs['Category'] = valid_pairs.apply(
            lambda row: '1' if row['Label1'] == 1 and row['Label2'] == 1 else '-1',
            axis=1
        )

        # Save results
        output_file = os.path.join(output_dir, f'bleu_scores_with_category_{tissue_name}.csv')
        valid_pairs[['GSM1', 'GSM2', 'BLEU', 'Category']].to_csv(output_file, index=False)
        print(f"Results for tissue {tissue_name} saved to {output_file}.")

if __name__ == "__main__":
    main()
