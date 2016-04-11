import os, sys, subprocess
start=sys.argv[1]
for d, subdirs, files in os.walk(start):
    for f in files:
        if f.endswith('.fastq.qp'):
            fn=d+'/'+f
            nfn=fn.replace('.fastq.qp', '.fastq')
            cmd='quip -d '+fn+' > '+nfn
            ret=subprocess.call(cmd, shell=True)
            if ret==0:
                if os.path.exists(nfn):
                    os.remove(fpn)
            else:
                print "Failed on ", fn
                sys.exit(1)

            
