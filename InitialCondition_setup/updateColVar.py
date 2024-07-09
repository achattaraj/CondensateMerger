# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:28:39 2023

@author: chatt
"""
import numpy as np
import sys, re 
from numpy import mean, sqrt, array 

def calc_RadGy(posArr):
    # posArr = N,3 array for N sites
    com = mean(posArr, axis=0) # center of mass
    Rg2 = mean(np.sum((posArr - com)**2, axis=1))
    return com, sqrt(Rg2)  

def parseXYZfile(file):
    with open(file, 'r') as tf:
        lines = tf.readlines()
        
    tmp_arr = array([line.split() for line in lines[2:]])
    return tmp_arr[:,1:].astype(np.float32)

def getBoxDim(posArr):
    x,y,z = posArr[:,0], posArr[:,1], posArr[:,2]
    return round(max(x)-min(x)), round(max(y)-min(y)), round(max(z)-min(z))

def updateCV(cvfile, Rg, L):
    Rg = int(round(Rg))

    with open(cvfile, 'r') as tf:
        lines = tf.readlines()
    for i, line in enumerate(lines):
        if re.search('upperBoundary', line):
            lines[i] = f'\tupperBoundary {Rg + 15}\n'
        if re.search ('upperWalls', line):
            lines[i] = f'\tupperWalls {Rg + 10}\n'
    
    ofile = cvfile.split('.')[0]
    L2 = int(float(L)*2)
    ofile = f'{ofile}_L{L2}.colvars'

    with open(ofile, 'w') as tmpf:
        tmpf.writelines(lines)

_, xyzFile, cvfile, L = sys.argv


#file = '//wsl.localhost/Ubuntu/home/achattaraj/simData_WSL/lammps_sims/lammps_sim_setup/IC_N160.xyz'

posArr = parseXYZfile(xyzFile)

com, Rg = calc_RadGy(posArr)

updateCV(cvfile, Rg, L)

print()
print('File: ', xyzFile)

print(f'RadGy ~ {int(round(Rg))} A')

print('Dimension length (x,y,z): ', getBoxDim(posArr))


