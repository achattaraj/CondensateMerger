**b35_N200_L500.data:**  Initial condition of the system that defines 
- Number of atoms, bonds, angles
- Types of atoms, bonds, angles
- **10 extra bond per atom** tells the simulator to allocate extra memory for the reversible bonds that the sticker beads will form during the simulation
- Dimension of cubic simulation box
- Masses of the bead types
- Coordinate of the atoms
- Bonds (connectivity within chains)
- Angles (between permanently bonded beads)


**N200_Rg_L400.colvars**: Colvars (collective variable) file that define the bead IDs (middle bead of each chain) to compute the radius of gyration of the system. **fix colvars** module uses this file to run **metadynamics** simulation. 


**b35_N200_L500.in:** Input script for running Langevin Dynamics simulations using LAMMPS. Here we are modeling __dynamic bond formation__ between two polymer types.


## Simulation Overview
- **Temperature:** 310 Kelvin
- **Duration:** 100 million timesteps
- **Units:** Real (energy in kcal/mol, distance in Angstroms, etc.)
- **Boundary Conditions:** Periodic in all dimensions
- **Atom Style:** Full (considering molecular bonds and angles)
- **fName** is a string used to name output files

## Simulation Steps

**Initial condition:** Read initial configurations (atom positions, bonds, angles) from b35_N200_L500.data

### Force Fields and Interactions
- Neighbor lists are constructed with a 1.9 distance bin
- **Angle** force fields use a **cosine** functional form
- **Bonded interactions** are defined using a hybrid style combining **harmonic** and **harmonic/shift/cut**
- **Lennard-Jones** potential is used for **non-bonding** interactions with a cutoff of 25 Angstroms
- **bond/create/random** and **bond/break** commands manage the dynamic creation and breaking of bonds within defined types and groups, based on distance criteria

### Minimization and Equilibration

- The system is minimized to converge forces to 1.0e-4 and energies to 1.0e-6
- A Langevin thermostat is used for temperature control, incorporating stochastic dynamics with a damping parameter of 500
- The system is evolved using the NVE ensemble
- Perform the main simulation run for 100 million steps to observe clustering dynamics

### Output and Data Handling

- Generate detailed logs  **(${fName}.log)** and system thermodynamics reports **(Thermo_${fName}.dat)** 
- Periodically dump coordinates **(traj_${fName}.dump)** for trajectory visualization
- **BondData_${fName}.dat** tracks bond formations and breaks
- Periodically dump restart files **(${fName}_*.restart)** to save system's configurations which can be used to analyze the cluster topology 
- Execute balance (**comm_style tiled** and **fix balance**) and communication management to optimize parallel computation load
