# **Similarity Metrics Pipeline**
### *Comparing Text Descriptions Using BLEU, WMD, and Cosine Similarities*

---

## **Overview**

This repository provides a pipeline for calculating pairwise text similarities between biological sample and study descriptions. Given the ground truth labels for the samples, the pipeline computes similarities using the following methods:

- **BLEU Score (Bilingual Evaluation Understudy)**  
- **Word Mover's Distance (WMD)**  
- **Cosine Similarity**  

The workflow ensures comparisons occur only between samples from different experiments (GSEs).  

The results are used to evaluate how well these similarity metrics reflect the **true relationships between samples and studies**.

Note: I am starting with BLEU and will implement the rest of the mertics later
---

## **Project Structure (current)**

```plaintext
project_repo/
├── data/                            # Input and processed data
│   ├── processed_descriptions.tsv   # Preprocessed sample descriptions
│   └── similarity_results/          # Output folder for similarity scores
│
├── scripts/                         # Python scripts for similarity calculations
│   ├── calculate_bleu_scores.py          # Calculates BLEU scores
│   ├── filter_ground_truth_pairs_bleu.py # Filters BLEU pairs based on ground truth labels
│
├── bin/                             # Executable scripts and tools
│   ├── submit_bleu_job.sbatch       # SLURM script for BLEU similarity job arrays
│   └── readme.txt                   # Details about external tools and their setup
│
├── results/                         # Output results
│   ├── bleu_scores.csv.gz           # BLEU similarity scores
│   ├── filtered_pairs_bleu.csv.gz   # Ground truth filtered BLEU pairs
│
└── README.md                        # Project documentation (this file)



---
## **Project Structure (goal)**
project_repo/
├── data/                            # Input and processed data
│   ├── processed_descriptions.tsv   # Preprocessed sample descriptions
│   └── similarity_results/          # Output folder for similarity scores
│
├── scripts/                         # Python scripts for similarity calculations
│   ├── calculate_bleu_scores.py          # Calculates BLEU scores
│   ├── calculate_wmd_scores.py           # Calculates WMD similarity
│   ├── calculate_cosine_scores.py        # Calculates Cosine similarity
│   ├── filter_ground_truth_pairs_bleu.py # Filters BLEU pairs based on ground truth labels
│   ├── filter_ground_truth_pairs_wmd.py  # Filters WMD pairs based on ground truth labels
│   └── filter_ground_truth_pairs_cosine.py # Filters Cosine pairs based on ground truth labels
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
│   ├── filtered_pairs_bleu.csv.gz   # Ground truth filtered BLEU pairs
│   ├── filtered_pairs_wmd.csv.gz    # Ground truth filtered WMD pairs
│   └── filtered_pairs_cosine.csv.gz # Ground truth filtered Cosine pairs
│
└── README.md                        

