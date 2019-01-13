with open('rosalind_dna.txt') as input_data:
    dna = input_data.read()

nuc_count = []
for nucleotide in ['A', 'C', 'G', 'T']:
    nuc_count.append(str(dna.count(nucleotide)))
print ' '.join(nuc_count)

with open('output_DNA.txt', 'w') as output_data:
	output_data.write(' '.join(nuc_count))