import re, sys  
import numpy as np  

def writeInputFile(file, L=500, n=5, NA=100, NB=100):
    N_chain = NA + NB
    b = n*7
    lines = []
    with open(file, 'r') as tf:
        lines = tf.readlines()
        for i, line in enumerate(lines):
            if re.search('variable fName string', line):
                lines[i] = f'variable fName string N{N_chain}_L{L} \n'

            if re.search('read_data', line):
                lines[i] = f'read_data b{b}_N{N_chain}_L{L}.data extra/special/per/atom 10 \n'

            if re.search('fix CV_Rg all colvars', line):
                lines[i] = f'fix CV_Rg all colvars N{N_chain}_Rg_L{L}.colvars' + ' output ${fName} \n'

    
    with open(f'b{b}_N{N_chain}_L{L}' + '.in', 'w') as tmf:
        tmf.writelines(lines)



def writeSubmitScript(L, n=5, NA=100, NB=100):
    N_chain = NA + NB
    b = n*7
    infile = f'b{b}_N{N_chain}_L{L}' + '.in'

    with open(f'submit_N{N_chain}_L{L}.sh', 'w') as tf:
        tf.write('#!/bin/bash\n') 
        tf.write(f'#SBATCH --job-name=N{N_chain}_L{L}\n')
        tf.write(f'#SBATCH -n  28\n')
        tf.write('#SBATCH -t 3-00:00:00 # DD-HH:MM:SS\n')
        tf.write('#SBATCH -p sapphire\n')
        tf.write(f'#SBATCH --mem-per-cpu=400\n')
        tf.write('#SBATCH -o %x_%j.out\n')
        tf.write('#SBATCH -e %x_%j.err\n')
        tf.write('#SBATCH --mail-type=END\n')
        tf.write('#SBATCH --mail-user=achattaraj@fas.harvard.edu\n\n')
        tf.write('module load gcc/12.2.0-fasrc01 openmpi/4.1.4-fasrc01\n\n')
        tf.write(f'srun -n $SLURM_NTASKS --mpi=pmix /n/home07/achattaraj/lammps-5Jun19/src/lmp_mpi -in {infile} \n')
        
        

_, file, L, n, NA, NB = sys.argv 
writeInputFile(file, L, int(n), int(NA), int(NB)) 
writeSubmitScript(L, int(n), int(NA), int(NB))

