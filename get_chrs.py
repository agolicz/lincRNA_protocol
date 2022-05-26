from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import sys


with open(sys.argv[1]) as handle:
    for seq in SeqIO.parse(handle, "fasta"):
        gid="_A02"
        if(gid in seq.id):
            sys.stdout.write(seq.format("fasta"))
            sys.stdout.flush()

handle.close()
