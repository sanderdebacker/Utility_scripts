#!usr/bin/python3
#===============================================================================
# Description
#===============================================================================

# Yves BAWIN September 2019

#===============================================================================
# Import modules
#===============================================================================

import os, sys, argparse
from datetime import datetime

#===============================================================================
# Parse arguments
#===============================================================================

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description = 'Create a nexus file with gene tree topologies as input for a maximum likelihood analysis in Phylonet.')

#Mandatory arguments
parser.add_argument('-d', '--dir',
					type = str,
					help = 'Directory containing all Nexus tree files.')

#Optional arguments
parser.add_argument('-s', '--suffix',
					type = str,
					default = '.nexus.con.tre',
					help = 'Suffix of the Nexus tree files (default = .nexus.con.tre).')

# Parse arguments to a dictionary.
args = vars(parser.parse_args())

#===============================================================================
# Functions
#===============================================================================

def print_date ():
	"""
	Print the current date and time to stderr.
	"""
	sys.stderr.write('-------------------\n')
	sys.stderr.write('{}\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
	sys.stderr.write('-------------------\n\n')
	return


def Convert(tree, d = args['dir']):

    # Remove extensions (1) .tre and (2) .con and (3) .nex
    name = (os.path.splitext((os.path.splitext((os.path.splitext(tree))[0]))[0]))[0]
	
	#Create an output file.
    in_tree = open('{}/{}'.format(d, tree))
    out_tree = open('{}/{}.newick'.format(d, name), 'w+')
	
	#Create the variables names (boolean) and names_dict (dictionary).
    names, names_dict = False, dict()
	
    for l in in_tree:
        if l.startswith('begin trees;'):
            names = True
        if names == True:
            if not l.startswith('   tree'):
                l = list(filter(None, l.rstrip().split('\t')))
                if l[0].isnumeric():
                    names_dict[l[0]] = l[1].rstrip(',')
            elif l.startswith('   tree'):
                tr = l.rstrip()
                for number, taxon in names_dict.items():
                    tr = tr.replace(',{}[&prob'.format(number), ',{}[&prob'.format(taxon))
                    tr = tr.replace('({}[&prob'.format(number), '({}[&prob'.format(taxon))
	
    #Extract sample name and branch lengths from tree.
    brackets = False
    new_tree = ''
    for i in tr[30:]:
        if i == '[':
            brackets = True
        if brackets == False:
            new_tree += i
        if i == ']':
            brackets = False
    print(new_tree, file = out_tree)
    return


#===============================================================================
# Script
#===============================================================================

if __name__ == '__main__':

	print_date()
	sys.stderr.write("* Converting Nexus tree files into Newick tree files ... \n\n")
	trees = [t for t in os.listdir(args['dir']) if t.endswith(args['suffix'])]
	for tree in trees:
		Convert(tree)
	print_date()
