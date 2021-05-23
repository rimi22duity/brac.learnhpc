#!/bin/bash
#SBATCH --job-name=parallel_job_pi    # Job name
#SBATCH --ntasks=2                    # Run on a single CPU
#SBATCH --mem=1gb                     # Job memory request
#SBATCH --time=00:05:00               # Time limit hrs:min:sec
#SBATCH --output=parallel_pi_%j.log   # Standard output and error log
module load Python
module load SciPy-bundle/2020.03-foss-2020a-Python-3.8.2
mpirun python mpi-pi.py 100
