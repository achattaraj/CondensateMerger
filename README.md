This repository is part of the study - "Separation of sticker-spacer energetics governs the coalescence of metastable biomolecular condensates". It contains files used to setup simulations and analyze the data.
- __InitialCondition_setup__ contains codes to create two types of polymer chains in a template based manner (using __MolTemplate__) and fill in 200 chains in a simulation box (using __packmol__)
  
- __N200_clustering__ contains files regarding the metadynamics simulation of 200 chains becoming one large cluster
  
- __TwoCluster_setup__ contains python scripts to a copy a cluster that serves as the initial condition for two-cluster fusion simulation
  
- __Two_cluster_fusion_S10N03kT__ contains files that exemplify metadynamics simulation of two cluster fusion at a given pair of energy parameters (Es = 10kT, Ens = 0.3kT). Similar simulations are performed for a range of parameter combinations
  
- __ClusterProperty__ contains python scripts used to analyze the biophysical properties of the cluster

