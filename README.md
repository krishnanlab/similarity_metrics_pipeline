# similarity_metrics_pipeline
Comparing Text Descriptions Using BLEU, WMD, and Cosine Similarities
Overview

This repository provides a pipeline for calculating pairwise text similarities between biological sample and study descriptions. Given the ground truth labels for the samples, the pipeline computes similarities using the following methods:

BLEU Score (Bilingual Evaluation Understudy)
Word Mover's Distance (WMD)
Cosine Similarity

The workflow ensures comparisons occur only between samples from different experiments (GSEs).

The results are used to evaluate how well these similarity metrics reflect the true relationships between samples and studies 


project_repo/
├── data/                            # Input and processed data
│   ├── processed_descriptions.tsv   # Preprocessed sample descriptions
│   └── similarity_results/          # Output folder for similarity scores
│
├── scripts/                         # Python scripts for similarity calculations
│   ├── calculate_bleu_scores.py      # Calculates BLEU scores
│   ├── calculate_wmd_scores.py       # Calculates WMD similarity
│   ├── calculate_cosine_scores.py    # Calculates Cosine similarity
│   ├── filter_ground_truth_pairs_bleu.py    # Filters pairs based on ground truth labels              
│   ├── filter_ground_truth_pairs_wmd.py     # Filters pairs based on ground truth labels  
│   └── filter_ground_truth_pairs_cosine.py  # Filters pairs based on ground truth labels                        
│
├── bin/                             # Executable scripts and tools
│   ├── submit_bleu_job.sbatch       # SLURM script for BLEU similarity job arrays
│   ├── submit_wmd_job.sbatch        # SLURM script for WMD similarity job arrays
│   ├── submit_cosine_job.sbatch     # SLURM script for Cosine similarity job arrays
│   └── readme.txt                   # Details about external tools and their setup
│
├── results/                         # Output results
│   ├── bleu_scores.csv.gz           # BLEU similarity scores
│   ├── wmd_scores.csv.gz            # WMD similarity scores
│   ├── cosine_scores.csv.gz         # Cosine similarity scores
│   └── filtered_pairs_bleu.csv.gz        # Ground truth filtered sample pairs
│   └── filtered_pairs_wmd.csv.gz  
│   └── filtered_pairs_cosine.csv.gz   
└── README.md                        # Project documentation (this file)



