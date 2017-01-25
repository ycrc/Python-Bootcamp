import sys
fp=open(sys.argv[1])
print (fp.readline().strip())
for l in fp:
   flds=l.strip().split(',')
   flds[4]=flds[4][:-3]
   print (','.join(flds))
