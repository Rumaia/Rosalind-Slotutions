from Methods import ReadFASTA

dna, sub_seq = [fasta[1] for fasta in ReadFASTA('rosalind_sseq.txt')]

sseq_indicies, i = [], 0
for nucleotide in sub_seq:
	# In practice: Use exception handling/additional constraints as such a subsequence does not necessarily exist.
	while dna[i] != nucleotide:
		i += 1

	# Use i+1 as the indicies because Rosalind starts at i=1 instead of i=0.
	sseq_indicies.append(str(i+1))
	i += 1

print ' '.join(sseq_indicies)
with open('output_SSEQ.txt', 'w') as output_data:
	output_data.write(' '.join(sseq_indicies))