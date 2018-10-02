from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# reference: http://biopython.org/DIST/docs/api/Bio.pairwise2-module.html

# Read sequences dataset to be aligned
file = open('in.txt', 'r')

sequence = ""
seq_count = 0
list_of_seqs = []

while 1:
    char = file.read(1)          # read by character
    
    
    if char == "\n":
    	continue
    elif char == ">" or not char:
    	if char: 
	    	list_of_seqs.append(sequence)
	    	seq_count = seq_count + 1
	    	print("new sequence is")
	    	sequence = ""
    	if not char: 
    		list_of_seqs.append(sequence)
    		sequence = ""
    		break
    elif char == "A" or char == "T" or char == "G" or char == "C":
    	sequence = sequence + char
    else:
    	continue
# print("parsed", seq_count)

# Get a list of the global alignments between the two sequences ACGGGT and ACG
# No parameters. Identical characters have score of 1, else 0.
# No gap penalties.

for i in range(1, 12 + 1):
	print("i is", i)
	for j in range(i+1, 12 + 1):
		similarity = pairwise2.align.globalxx(list_of_seqs[i], list_of_seqs[j])
		print(i, " and ", j, " have ", len(similarity), " alignments")
