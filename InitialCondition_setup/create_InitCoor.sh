n=5 # segment count
seg=2221222 # segment pattern

NA=100 # A-chain count
NB=100 # B-chain count 
#L=300 # 
for L in 250 
do 
L2=$((2*$L))

pck_inp='populate_tmp.inp'

pck_out='IC_tmp.xyz' 

sysName="b35_N200_L$L2.lt" # double quote is needed for bash 

dataFile="b35_N200_L$L2.data"

python3 LT_writer.py $n $seg 

python3 writePackmolInput.py $n $NA $NB $L $pck_inp $pck_out

python3 writeSysLT.py $n $NA $NB $L $sysName

packmol < $pck_inp

moltemplate.sh -xyz $pck_out $sysName -nocheck

done 

