# -*- coding: utf-8 -*-
"""
@author: Ani Chattaraj
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import mean, pi, array 
import re 

font = {'family' : 'Arial',
        'size'   : 16}

plt.rc('font', **font)


def calc_RadGy(posList):
    # posList = N,3 array for N sites
    com = np.mean(posList, axis=0) # center of mass
    Rg2 = np.mean(np.sum((posList - com)**2, axis=1))
    return com, np.sqrt(Rg2) 

def readFile(file):
    with open(file,'r') as tf:
        lines = tf.readlines()
    return lines 

def getBlock(lines, str1='', str2='', skipName=True):
    # skipName => whether to return heading  
    i1, i2 = 0, 0
    for i, line in enumerate(lines):
        if re.search(str1, line):
            i1 = i 
        if re.search(str2, line):
            i2 = i 
    if str2 == '':
        i2 = len(lines)
        
    if skipName:
        return lines[i1+1:i2]
    else:
        return lines[i1:i2]

def processCoorBlock(cBlock):
    tmp_frame = array([line.strip().split() for line in cBlock[1:-1]])
    atomId = tmp_frame[:,0].astype(np.int32)
    atomTyp = tmp_frame[:,2].astype(np.int32)
    charge = tmp_frame[:,3].astype(np.float32)
    mId = tmp_frame[:,1].astype(np.int32)
    pos = tmp_frame[:,[4,5,6]].astype(np.float32)
    return atomId, mId, atomTyp, charge, pos, max(atomId), max(mId)

def processBondBlock(bBlock):
    tmp_frame = array([line.strip().split() for line in bBlock[1:-1]])
    bId = tmp_frame[:,0].astype(np.int32)
    bTyp = tmp_frame[:,1].astype(np.int32)
    bPair = tmp_frame[:,[-2,-1]].astype(np.int32)
    return bId, bTyp, bPair, max(bId)  

def processAngleBlock(aBlock):
    tmp_frame = array([line.strip().split() for line in aBlock[1:]])
    aId = tmp_frame[:,0].astype(np.int32)
    aTyp = tmp_frame[:,1].astype(np.int32)
    angle = tmp_frame[:,[2,3,4]].astype(np.int32)
    return aId, aTyp, angle, max(aId)  
    
def copyCoorBlock(cBlock, dist=300):
    # dist: distance between two clusters along z direction
    atomId, mId, atomTyp, charge, pos, aCount, mCount   = processCoorBlock(cBlock)
    
    # first copy 
    aId1 = atomId[:, np.newaxis] # row to column vector
    mId1 = mId[:, np.newaxis]
    charge1 = charge[:, np.newaxis]
    aTyp1 = atomTyp[:, np.newaxis]
    cluster1 = np.concatenate((aId1,mId1,aTyp1,charge1,pos), axis=1)
    
    # second copy 
    aId2 = (atomId + aCount)[:, np.newaxis] # row to column vector
    mId2 = (mId + mCount)[:, np.newaxis]
    charge2 = charge[:, np.newaxis]
    aTyp2 = atomTyp[:, np.newaxis]

    pos2 = np.copy(pos)
    
    c1, Rg1 = calc_RadGy(pos)
    
    dist = 3*Rg1

    pos2[:,2] = pos[:,2] + dist
    
    c2, Rg2 = calc_RadGy(pos2)
    

    print(f'Radius of Gyration of the Cluster : {Rg1:.2f} A')
    
    cluster2 = np.concatenate((aId2,mId2,aTyp2,charge2,pos2), axis=1)
    
    return np.concatenate((cluster1, cluster2), axis=0), (c1,c2), Rg1
    
def copyBondBlock(bBlock, cBlock):
    atomId, mId, atomTyp, charge, pos, aCount, mCount   = processCoorBlock(cBlock)
    bId, bTyp, bp, bCount = processBondBlock(bBlock)
    # first copy 
    bId1 = bId[:, np.newaxis] # row to column vector
    bTyp1 = bTyp[:, np.newaxis]
    cluster1 = np.concatenate((bId1, bTyp1, bp), axis=1)
    # second copy 
    bId2 = (bId + bCount)[:, np.newaxis] 
    bTyp2 = bTyp[:, np.newaxis]
    bp2 = bp + aCount 
    cluster2 = np.concatenate((bId2, bTyp2, bp2), axis=1)
    
    return np.concatenate((cluster1, cluster2), axis=0)
    
def copyAngleBlock(aBlock, cBlock):
    atomId, mId, atomTyp, charge, pos, atomCount, mCount  = processCoorBlock(cBlock)
    aId, aTyp, angle, aCount = processAngleBlock(aBlock)
    # first copy 
    aId1 = aId[:, np.newaxis] # row to column vector
    aTyp1 = aTyp[:, np.newaxis]
    cluster1 = np.concatenate((aId1, aTyp1, angle), axis=1)
    # second copy 
    aId2 = (aId + aCount)[:, np.newaxis] 
    aTyp2 = aTyp[:, np.newaxis]
    angle2 = angle + atomCount 
    cluster2 = np.concatenate((aId2, aTyp2, angle2), axis=1)

    return np.concatenate((cluster1, cluster2), axis=0)
    
def writeLines(fileStream, Lines, arr=True):
    if arr:
        for line in Lines:
            fileStream.writelines([f'{l} ' for l in line])
            fileStream.write('\n')
    else:
        fileStream.writelines([f'{line} ' for line in Lines])
        fileStream.write('\n')

def writeFile(fName, mB, cB, bB, aB, centers, Rg):
    # fileName, mass, coordinates, bond, angle (block), 
    # centers of two clusters, RadGy of the clusters
    atomCount, _ = cB.shape
    bondCount, _ = bB.shape 
    angleCount, _ = aB.shape 
    
    atomTypes = len(set(cB[:,2]))
    bTypes = len(set(bB[:,1]))
    aTypes = len(set(aB[:,1]))
    
    c1, c2 = centers 
    
    x1, y1, z1 = c1 
    x2, y2, z2 = c2 
    bound = Rg + 200
    
    x_low = int(x1 - bound) 
    x_hi = int(x1 + bound) 
    y_low = int(y1 - bound) 
    y_hi = int(y1 + bound) 
    
    z_min, z_max = min(z1, z2), max(z1,z2)
    
    z_low = int(z_min - Rg - 100) 
    z_hi = int(z_max + Rg + 100)
    
    CV_max = (z_hi - z_low) - 2*Rg 
    #print('ColVar_max along Z: ', round(CV_max))
    
    with open(fName, 'w') as of:
        of.write('LAMMPS Description \n\n')
        of.write(f'{atomCount}  atoms\n')
        of.write(f'{bondCount}  bonds\n')
        of.write(f'{angleCount}  angles\n\n')
        
        of.write(f'{atomTypes}  atom types\n')
        of.write(f'{bTypes}  bond types\n')
        of.write('10 extra bond per atom\n')
        of.write(f'{aTypes}  angle types\n\n')
        
        of.write(f'{x_low} {x_hi} xlo xhi\n')
        of.write(f'{y_low} {y_hi} ylo yhi\n')
        of.write(f'{z_low} {z_hi} zlo zhi\n\n')
        
        writeLines(of, mB, arr=False)
        
        of.write('Atoms\n\n')
        #writeLines(of, cB[:])
        # converting atomID, Type and molID into intergers
        cList = [[int(e[0]), int(e[1]), int(e[2]), e[3],e[4],e[5],e[6]] for e in cB]
        writeLines(of, cList)
        
        of.write('\nBonds\n\n')
        writeLines(of, bB[:])
        
        of.write('\nAngles\n\n')
        writeLines(of, aB[:])
        
    
    print('Copied the cluster and wrote the data in ', fName)

    







