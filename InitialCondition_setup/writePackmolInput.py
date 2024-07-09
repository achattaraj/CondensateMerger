# arguments - n (segment count), NA (count of A-polymer), NB, Box Length (L), input fileName, xyz output filename
import sys 

_, n, NA, NB, L, inp_file, outfile = sys.argv 
n, NA, NB, L = int(n), int(NA), int(NB), float(L)

L = L - 10

with open(f'{inp_file}', 'w') as tf:
	tf.write('tolerance  5\n')
	tf.write('seed       457\n\n')
	tf.write('filetype xyz\n')
	tf.write(f'output  {outfile}\n\n')

	tf.write(f'structure polyA_n{n}_mono.xyz\n')
	tf.write(f'\tnumber {NA}\n')
	tf.write(f'\tinside box  {-L}  {-L} {-L}  {L} {L} {L}\n')
	tf.write('end structure\n\n')

	tf.write(f'structure polyB_n{n}_mono.xyz\n')
	tf.write(f'\tnumber {NB}\n')
	tf.write(f'\tinside box  {-L}  {-L} {-L}  {L} {L} {L}\n')
	tf.write('end structure\n')






