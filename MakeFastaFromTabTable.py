#!/usr/bin/python3

barcodes = "Barcodes.txt"

with open("TableOfBarcodesAA.fasta", "w+") as f:
    for line in open(barcodes):
        print(line)
        line = line.rstrip().split('\t')
        name = line[0]
        barcode = line[1]
        print('>{}\n{}'.format(name, barcode), file=f)