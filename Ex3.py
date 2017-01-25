'''
Example 3
This script reads a file containing genes and contructs a lookup table
It then reads a file containing mapped reads and finds the genes
overlapping with each read.
'''

import sys
from intervaltree import IntervalTree

print("initializing table")
table={}
# sys.argv=['dummy', 'genes.txt', 'mappedreads.txt'] # for Jupyter
for line in open(sys.argv[1]):
    genename, chrm, strand, start, end = line.split()
    if not chrm in table:
        table[chrm]=IntervalTree()
    table[chrm][int(start):int(end)]=genename
print("done")

print=("reading sequences")

for line in open(sys.argv[2]):
    name, chrm, pos, seq = line.strip().split()
    genes=table[chrm][int(pos):int(pos)+len(seq)]
    if genes:
        print(name, chrm, pos, seq)
        for gene in genes:
            print('\t',gene.data)

