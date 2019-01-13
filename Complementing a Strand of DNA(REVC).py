from string import maketrans

with open('rosalind_revc.txt') as input_data:
	dna = input_data.read()

nucleotide = 'ATCG'
complement = 'TAGC'
transtab = maketrans(nucleotide, complement)
dna_reverse_complement = dna.translate(transtab)[::-1].lstrip()

with open('output_REVC.txt', 'w') as output_data:
	output_data.write(dna_reverse_complement)