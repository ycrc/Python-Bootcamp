import sys
from intervaltree import IntervalTree

print "initializing"
genefinder={}
for line in open(sys.argv[1]):
    genename, chrm, strand, start, end = line.split()[0:5]    
    if not chrm in genefinder:
        genefinder[chrm]=IntervalTree()
    genefinder[chrm][int(start):int(end)]=genename

print "reading sequences"
for line in open(sys.argv[2]):
    tag, flag, chrm, pos, mapq, cigar, rnext, pnext, tlen, seq, qual = line.split()[0:11]
    genes=genefinder[chrm][int(pos):int(pos)+len(seq)]
    if genes:
        print tag
        for gene in genes:
            print '\t',gene.data



