Open a terminal and run the shell script __"create_InitCoor.sh"__

1. The quantity __seg__ defines the sticker-spacer pattern as a block (2: spacer, 1;sticker)

2. __n__ is segement count. There are 7 beads in a segment and there 5 such segments; henece 7 * 5 = 35 beads in a chain 

3. __"LT_writer.py"__ creates molecular templates (polyA_n5.lt and polyB_n5.lt) which define all the atoms, bonds and angles inside a chain. It also creates initial locations of chain beads in the form of 'xyz' files (polyA_n5_mono.xyz, polyB_n5_mono.xyz)

4. packmol input __"populate_tmp.inp"__ packs 100 chain-A and 100 chain-B into a cubic box (L = 500 A). It creates a "xyz" file (__IC_tmp.xyz__) containing coordinates for 200 chains. 

5. __"Moltemplate.sh"__ takes the IC_tmp.xyz file as input and creates the datafile __"b35_N200_L500.data"__ which can be used as the configuration file for LAMMPS simulation. 
