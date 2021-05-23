#!/bin/bash
#SBATCH --job-name=serial_job_pi    # Job name
#SBATCH --mail-type=END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --ntasks=1                    # Run on a single CPU
#SBATCH --mem=1gb                     # Job memory request
#SBATCH --time=00:05:00               # Time limit hrs:min:sec
#SBATCH --output=serial_pi_%j.log   # Standard output and error log
module load Python
module load SciPy-bundle/2020.03-foss-2020a-Python-3.8.2
python pi.py 100
