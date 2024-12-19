#!/bin/bash

#SBATCH --job-name=BLEU_calc            # Job name
#SBATCH --output=bleu_calc.%j.out       # Standard output log
#SBATCH --error=bleu_calc.%j.err        # Standard error log
#SBATCH --time=04:00:00                 # Maximum runtime 
#SBATCH --ntasks=1                      # Number of tasks
#SBATCH --cpus-per-task=2               # Number of CPUs per task
#SBATCH --mem=16G                        # Memory per node (8 GB)

# Run the Python script
python src/calculate_bleu_scores.py
