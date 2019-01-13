from Methods import ReadFASTA

dna1, dna2 = [fasta[1] for fasta in ReadFASTA('rosalind_tran.txt')]

transitions = transversions = 0.0
for i in xrange(len(dna1)):
	if dna1[i] == dna2[i]:
		pass
	# Check if the nucleotides are in the same purine/pyrimidine group.
	elif dna1[i] in [['A', 'G'],['C', 'T']][dna2[i] in ['C', 'T']]:
		transitions += 1
	else:
		transversions +=1

print transitions/transversions
with open('output_TRAN.txt', 'w') as output_data:
	output_data.write(str(transitions/transversions))