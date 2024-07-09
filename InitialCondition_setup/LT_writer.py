# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 11:35:30 2022

@author:Ani Chattaraj
"""
import numpy as np 
import sys

# this file takes two additional arguments from command line - segment count (n) and segment pattern (stickers-spacers)  

def writeXYZ(molName, seq, typName):
    print(f'Writing XYZ file for {molName} monomer ...')
    with open(f'{molName}_mono.xyz', 'w') as tf:
        tf.write(f'{len(seq)}\n')
        tf.write(f'{molName}\n')
        xcoor = 5 
        for bead in seq:
            tf.write(f'{typName[bead]}      {xcoor}      0     0\n')
            xcoor += 5
    print('... done!')
    print()

def writePolyLT(molName, seq, typName, mass):
    print(f'Writing LT file for {molName} ...')
    idList = np.arange(1, len(seq)+1, 1)
    N_bds = len(seq) # number of beads per molecule
    qList = [0]*N_bds # charge of beads
    with open(f'{molName}.lt', 'w') as tf:
        tf.write(f'{molName}' + ' {\n\n')
        
        tf.write('write_once("Data Masses") { \n')
        for typ,name in typName.items():
            tf.write(f'@atom:{name}  {mass[typ]}\n')
        tf.write('} \n\n')
        
        tf.write('write("Data Atoms") { \n')
        for i, bead in enumerate(seq):
            tf.write(f'$atom:{i+1} $mol:. @atom:{typName[seq[i]]} {qList[i]} 0 0 0\n')
        tf.write('} \n\n')
        
        tf.write('write("Data Bonds") { \n')
        for i in range(N_bds - 1):
            tf.write(f'$bond:b{i+1}    @bond:Bond   $atom:{idList[i]}  $atom:{idList[i+1]}\n') 
        tf.write('} \n\n')
        
        tf.write('write("Data Angles") { \n')
        for i in range(N_bds - 2):
            tf.write(f'$angle:a{i+1}    @angle:Angle   $atom:{idList[i]}  $atom:{idList[i+1]}  $atom:{idList[i+2]}\n')
        tf.write('} \n\n')
        
        tf.write('} \n' + f'#{molName}')
        
    print('... done!')
    print()
    
_, n, pat = sys.argv 
n = int(n)
seg = [int(i) for i in pat]
print('Segment pattern: ', seg)
print('Segment count: ', n)
seq = [seg]*n
seq = np.array(seq).flatten()

# first molecule
fName1 = f'polyA_n{n}'
typName1 = {1:'A', 2:'AL'}
mass1 = {1:1000, 2: 1000}
writePolyLT(fName1, seq, typName1, mass1)
writeXYZ(fName1, seq, typName1)

# second molecule    
fName2 = f'polyB_n{n}'
typName2 = {1:'B', 2:'BL'}
mass2 = {1: 1000, 2: 1000}
writePolyLT(fName2, seq, typName2, mass2)
writeXYZ(fName2, seq, typName2)


        
        
        
        
        
    
    


 