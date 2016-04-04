import sys
from intervaltree import IntervalTree
from collections import defaultdict

class ChrRec(object):
    def __init__(self):
        self.it=IntervalTree() # holds gene intervals
        self.genes=defaultdict(list) # holds a list of sequences for each gene
    def addGene(self, genename, genestart, geneend):
        self.it.addi(genestart, geneend, genename)
    def getGenes(self, readstart, readend):
        genes=self.it.search(readstart, readend)
        return [gene.data for gene in genes]
    def insertSeq(self, start, end, seq):
        for genename in self.getGenes(start, end):
            self.genes[genename].append(seq)
    def getSeqs(self, genename):
        return self.genes[genename]

if __name__=='__main__':
    print "initializing"
    genefinder=defaultdict(ChrRec)

    for line in open(sys.argv[1]):
        genename, chrm, strand, start, end = line.split()[0:5]    
        genefinder[chrm].addGene(genename, int(start), int(end))

    print "reading sequences"
    for line in open(sys.argv[2]):
        tag, flag, chrm, pos, mapq, cigar, rnext, \
            pnext, tlen, seq, qual = rd = line.split()[0:11]
        genefinder[chrm].insertSeq(int(pos), int(pos)+len(seq), rd)

    print genefinder['chr4'].genes

