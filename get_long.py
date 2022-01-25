from Bio import SeqIO
import sys

for seq in SeqIO.parse(sys.argv[1], "fasta"):
    if(len(seq.seq)>=200):
        print(seq.id)
