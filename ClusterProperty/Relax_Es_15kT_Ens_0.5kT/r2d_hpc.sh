#!/bin/bash
#SBATCH --job-name=r2d
#SBATCH -n  1 #Number of cores
#SBATCH -t 0-02:00:00 # Amount of time needed DD-HH:MM:SS
#SBATCH -p test # Partition to submit to
#SBATCH --mem-per-cpu=400
#SBATCH --mail-type=NONE
#SBATCH --mail-user=chattarajaniruddha@gmail.com

module load gcc/12.2.0-fasrc01 openmpi/4.1.4-fasrc01
for FILE in *.restart
do 
	echo Current file is $FILE
	dFILE=${FILE/.restart/.DATA}
	echo $dFILE
	srun -n 1 --mpi=pmix /n/home07/achattaraj/lammps-5Jun19/src/lmp_mpi -restart2data $FILE $dFILE

done 