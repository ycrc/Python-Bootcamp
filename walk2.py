
import os, sys, subprocess

start=sys.argv[1]
for d, subdirs, files in os.walk(start):
    for f in files:
        if f.endswith('.fastq.qp'):
            fp=d+'/'+f
            nfp=fp.replace('fastq.qp', '.fastq')
            cmd='quip -d '+fp+' > '+nfp
            ret=subprocess.call(cmd, shell=True)
            if ret: # True means failed
                print "Failed on ", fp
                break
            else:
                os.remove(fp)
                
            
            
