## Dynamic bond (crosslink) formation between sticker-spacer polymer chains in LAMMPS

This repository is part of the study - **"Separation of sticker-spacer energetics governs the coalescence of metastable biomolecular condensates"**. It contains files used to setup simulations and analyze the data.

The repository is organized in order of the simulation pipeline: 

__1. InitialCondition_setup__ contains codes to create two types of polymer chains in a template based manner (using __MolTemplate__) and fill in 200 chains in a simulation box (using __packmol__). The script create_InitCoor.sh executes these codes to create initial data file to start LAMMPS simulations.
  
__2. N200_clustering__ contains files regarding the metadynamics simulation of 200 chains becoming one large cluster. The [README](https://github.com/achattaraj/CondensateMerger/blob/main/N200_Clustering/README.md) file contains detailed descriptions about the simulation setup and execution.
  
__3. TwoClusterSetUp_v2.ipynb__  is a python notebook with code that copies the cluster created by the initial simulations (N200_clustering), and creates datafile containing two identical side-by-side clusters in a proportionally larger simulation box. This datafile is then used as initial conditions for two-cluster fusion simulation. 
  
__4. Two_cluster_fusion_S10N03kT__ contains files that exemplify metadynamics simulation of two-cluster fusion at a given pair of energy parameters (Es = 10kT, Ens = 0.3kT). Similar simulations are performed for a range of parameter combinations.
  
__5. ClusterProperty__ contains python scripts used to analyze the biophysical properties of the cluster.


## Useful Links
- [How to run LAMMPS](https://docs.lammps.org/Run_head.html)
- [bond_style harmonic/shift/cut](https://docs.lammps.org/bond_harmonic_shift_cut.html) (Note: This bond style can only be used if LAMMPS was built with the EXTRA-MOLECULE package)
- [bond formation in LAMMPS](https://www.afs.enea.it/software/lammps/doc17/html/fix_bond_create.html). The modified version (**bond/create/random**) can be found in this [article](https://pubs.aip.org/aip/jcp/article-abstract/142/13/134102/901994/A-parallel-algorithm-for-step-and-chain-growth?redirectedFrom=fulltext) 
