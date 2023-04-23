#!/usr/bin/python3
import os,math,sys, shutil

## Please tell me your jobtype
jobtype = int(input("please input your job type(1.TS? 2.opt? 3.freq? 4.scan? 5.irc? 6.sp?) with \n"))

### the following two lines read your .xyz file and store its name 
ifs_name= sys.argv[1]

## generate new names for chk and com file according to the jobtypes
if jobtype == 1:
   ofs_name=ifs_name[:-4]+'_TS.com'
   chk_name=ifs_name[:-4]+'_TS.chk'

elif jobtype == 2:
   ofs_name=ifs_name[:-4]+'_opt.com'
   chk_name=ifs_name[:-4]+'_opt.chk'

elif jobtype == 3:
   ofs_name=ifs_name[:-4]+'_freq.com'
   chk_name=ifs_name[:-4]+'_freq.chk'

elif jobtype == 4:
   ofs_name=ifs_name[:-4]+'_scan.com'
   chk_name=ifs_name[:-4]+'_scan.chk'

elif jobtype == 5:
   ofs_name=ifs_name[:-4]+'_irc.com'
   chk_name=ifs_name[:-4]+'_irc.chk'
elif jobtype == 6:
   ofs_name=ifs_name[:-4]+'_sp.com'
   chk_name=ifs_name[:-4]+'_sp.chk'
else:
   print("no such xyz/chk file ")
   sys.exit()
   
 
### open your xyz file 
ifs = open(ifs_name, 'r')

### create a list for coordinates, then read all lines(atom and xyz) into this list
readxyz = input("if you want to load xyz then type 1; if load chk file type 0! \n")

if int(readxyz): 
   xyz_cor=[]
   for line in ifs.readlines()[2:]:
       xyz_cor.append(line)
   ifs.close()


### create and open new com file.
ofs=open(ofs_name,'w')

### write all informations into your com file.
### how many gb for memmory?
ofs.write('%mem=120gb \n')

### how many cores?
ofs.write('%nprocshared=28 \n')

### write your the name of your chk file 
ofs.write('%chk=' + chk_name + '\n')

### write functional, basis set and keywords
if jobtype == 1:
   if int(readxyz):
      ofs.write('#p B3LYP/gen opt=(calcfc,ts,noeigentest) \n')
   else:
      ofs.write('#p B3LYP/gen opt=(readfc,ts,noeigentest) geom=check guess=read \n')

elif jobtype == 2:
     if int(readxyz):
        ofs.write('#p B3lyp/gen opt \n')
     else:
        ofs.write('#p b3lyp/gen opt=readfc geom=check guess=read \n')

elif jobtype == 3:
     if int(readxyz):
        ofs.write('#p b3lyp/gen freq \n')
     else:
        ofs.write('#p b3lyp/gen freq geom=check guess=read\n')

elif jobtype == 4:
     if int(readxyz):
        ofs.write('#p b3lyp/gen opt=(modredundant,maxcycle=15) \n')
     else:
        ofs.write('#p b3lyp/gen opt=(modredundant,maxcycle=15) geom=check guess=read \n')

elif jobtype == 5:
     if int(readxyz):
        ofs.write('#p b3lyp/gen irc=(calcfc,MaxPoints=20,stepsize=10) nosym  \n')
     else:
        ofs.write('#p b3lyp/gen irc=(ReadCartesianFC,MaxPoints=20,stepsize=10) nosym geom=check guess=read \n')

elif jobtype == 6:
     if int(readxyz):
        ofs.write('#p b3lyp/gen sp \n')
     else:
        ofs.write('#p b3lyp/gen sp geom=check guess=read\n')

else:
   pass

ofs.write('\n')

### write your comment line
ofs.write('comment  \n')

ofs.write('\n')

### write your charge and multiplicity
ofs.write('0 2 \n')

### write all lines from your list into com file if load xyz; 
### otherwise copy check file and rename it.
if int(readxyz):
   for line in xyz_cor:
       ofs.write(str(line))
else:
   shutil.copy(ifs_name, chk_name)

### write an space line
ofs.write('\n')

### your gen basis set
ofs.write('C N O H Na Cl 0\n')
ofs.write('6-311G*\n')
ofs.write('****\n')
ofs.write('Co 0\n')
ofs.write('def2svp\n')
ofs.write('****\n')

### write an space line
ofs.write('\n')


ofs.close()
