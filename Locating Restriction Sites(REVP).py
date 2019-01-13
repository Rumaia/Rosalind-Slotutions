from Methods import ReadFASTA, ReverseComplementDNA

dna = ReadFASTA('rosalind_revp.txt')[0][1]
locations = []

for length in range(4,13):
	for index in range(len(dna)-length+1):
		if dna[index:index+length] == ReverseComplementDNA(dna[index:index+length]):
			print index+1, length
			locations.append(str(index+1)+' '+str(length))

with open('output_REVP.txt', 'w') as output_data:
	for location in locations:
		output_data.write(location+'\n')