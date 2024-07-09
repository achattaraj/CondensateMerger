import re, sys  
import numpy as np  

def writeDataFile(file):
    lines = []
    with open(file, 'r') as tf:
        lines = tf.readlines()
        for i, line in enumerate(lines):
            if re.search('bond types', line):
                bCount = float(line.split()[0])
                bCount = int(bCount) + 1
                lines[i] = f'{bCount}  bond types\n10 extra bond per atom\n'
                
    with open(file, 'w') as tmf:
        tmf.writelines(lines)

_, file = sys.argv 
writeDataFile(file) 