#!/usr/bin/python
import os,math,sys

jobtype = str(input("please input your job type(ts? opt? freq? scan? irc?) with \'  \' \n"))

ifs_name= sys.argv[1]
ifs = open(ifs_name, 'r')


xyz_cor=[]

for line in ifs.readlines()[2:]:
    xyz_cor.append(line)
ifs.close()

if jobtype == 'ts':
   ofs_name=ifs_name[:-4]+'_xTS.com'
   chk_name=ifs_name[:-4]+'_xTS.chk'

elif jobtype == 'opt':
   ofs_name=ifs_name[:-4]+'_xopt.com'
   chk_name=ifs_name[:-4]+'_xopt.chk'

elif jobtype == 'freq':
   ofs_name=ifs_name[:-4]+'_xfreq.com'
   chk_name=ifs_name[:-4]+'_xfreq.chk'

elif jobtype == 'scan':
   ofs_name=ifs_name[:-4]+'_xscan.com'
   chk_name=ifs_name[:-4]+'_xscan.chk'

elif jobtype == 'irc':
   ofs_name=ifs_name[:-4]+'_xirc.com'
   chk_name=ifs_name[:-4]+'_xirc.chk'

else:
   pass
 

ofs=open(ofs_name,'w')
ofs.write('%mem=32gb \n')
ofs.write('%nprocshared=28 \n')
ofs.write('%chk=' + chk_name + '\n')

### Your xtb.sh local path###
xtb_path = '/gsfs0/data/xuhq/gau_xtb_2/xtb.sh' 

if jobtype == 'ts':
   ofs.write('# opt(ts,calcall,noeigen,nomicro) external=\'' + xtb_path)
   ofs.write('\' \n')

elif jobtype == 'opt':
   ofs.write('# opt  external=\'' + xtb_path +'\' \n')

elif jobtype == 'freq':
   ofs.write('# freq external=\'' + xtb_path + '\' \n')
 
elif jobtype == 'scan':
   ofs.write('#  fopt=(nomicro,modredundant) external=\'' + xtb_path )
   ofs.write('\' \n')

elif jobtype == 'irc':
   ofs.write('# IRC(maxpoints=20,calcall) external=\'' + xtb_path + '\' \n')


else:
   pass

ofs.write('\n')
ofs.write('comment  \n')
ofs.write('\n')
ofs.write('0 2 \n')
for line in xyz_cor:
    ofs.write(str(line))
ofs.write('\n')
ofs.write('\n')
ofs.write('\n')


ofs.close()
