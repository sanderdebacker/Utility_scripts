#!/usr/bin/python3

from Bio import SeqIO

with open("output.fasta", "a") as f:
    for record in SeqIO.parse('file.fasta', 'fasta'):
        print('>{}\t{}'.format(record.description, record.seq), file=f)
    