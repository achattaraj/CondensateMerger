Input script for running Langevin Dynamics simulations using LAMMPS. Here we are modeling __dynamic bond formation__ between two polymer types.

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

### Minimization and Equilibration:

- The system is minimized to converge forces to 1.0e-4 and energies to 1.0e-6
- A Langevin thermostat is used for temperature control, incorporating stochastic dynamics with a damping parameter of 500
- The system is evolved using the NVE ensemble
- Perform the main simulation run for 100 million steps to observe clustering dynamics

### Output and Data Handling:

- Generate detailed logs  **(${fName}.log)** and system thermodynamics reports **(Thermo_${fName}.dat)** 
- Periodically dump coordinates **(traj_${fName}.dump)** for trajectory visualization
- **BondData_${fName}.dat** tracks bond formations and breaks.
- Execute balance and communication management to optimize parallel computation load
