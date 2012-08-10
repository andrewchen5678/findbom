#!/usr/bin/python
import os
import sys
#if len(sys.argv)<=1: workdir=os.getcwd()
#else: workdir=os.path.abspath(sys.argv[1])
if len(sys.argv)<=1: 
	print """usage: findbom.py directoryname"""
	exit(1);
else: workdir=os.path.normpath(sys.argv[1])
print "finding php files with bom in ",workdir
count=0
for root, dirs, files in os.walk(workdir):
    for name in files:
        if name[-4:] == '.php':
            filename = os.path.join(root, name)
            #print filename
            f=open(filename,'r')
            #f.seek(0)
            header=f.read(3)
            if header=='\xef\xbb\xbf':
				print filename,'has bom character'
				count=count+1
            f.close()
print count,"found in total"
