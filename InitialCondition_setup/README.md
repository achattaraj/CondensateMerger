Open a terminal and run the shell script "create_InitCoor.sh"

1. The quantity seg defines the sticker-spacer pattern as a block (2: spacer, 1;sticker)

2. n is segement count. There are 7 beads in a segment and there 5 such segments; henece 7 * 5 = 35 beads in a chain 

3. "LT_writer.py" creates molecular templates (polyA_n5.lt and polyB_n5.lt) which define all the atoms, bonds and angles inside a chain. It also creates initial locations of chain beads in the form of 'xyz' files (polyA_n5_mono.xyz, polyB_n5_mono.xyz)

4. packmol input "populate_tmp.inp" packs 100 chain-A and 100 chain-B into a cubic box (L = 500 A). It creates a "xyz" file (IC_tmp.xyz) containing coordinates for 200 chains. 

5. "Moltemplate.sh" takes the IC_tmp.xyz file as input and creates the datafile "b35_N200_L500.data" which can be used as the configuration file for LAMMPS simulation. 