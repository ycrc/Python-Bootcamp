import os, sys, subprocess
# sys.argv=['Ex2.py', 'Ex2dir'] # for Jupyter we'll cheat
start=sys.argv[1] 
for d, subdirs, files in os.walk(start):
    for f in files:
        if f.endswith('.fastq'):
            fn=d+'/'+f
            nfn=fn.replace('.fastq', '.fastq.gz')
            cmd='gzip -c '+fn+' > '+nfn
            print ("running", cmd)
            ret=subprocess.call(cmd, shell=True)
            if ret==0:
                if os.path.exists(nfn):
                    os.remove(fn)
            else:
                print ("Failed on ", fn)
                sys.exit(1)
print("Done")
