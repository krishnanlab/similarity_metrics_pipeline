#!/bin/bash
#SBATCH --job-name=filter_bleu_CL0000000
#SBATCH --output=run/logs/CL0000000_out.log
#SBATCH --error=run/logs/CL0000000_err.log
#SBATCH --time=01:00:00
#SBATCH --mem=8G

module load python/3.8

# Define paths
TISSUE_LABELS="bin/tissue_labels_CL:0000000.csv"
BLEU_SCORES="data/bleu_scores.csv.gz"
OUTPUT_DIR="results/bleu_scores_with_category"
SRC_SCRIPT="src/filter_bleu_scores_by_tissue.py"

# Run the filtering script for the specific tissue file
python $SRC_SCRIPT \
    --tissue_labels $TISSUE_LABELS \
    --bleu_scores $BLEU_SCORES \
    --output_dir $OUTPUT_DIR
