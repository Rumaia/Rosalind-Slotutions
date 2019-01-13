with open('rosalind_rna.txt') as input_data:
    dna = input_data.read().strip()

with open('output_RNA.txt', 'w') as output_data:
    output_data.write(dna.replace('T', 'U'))
    print dna.replace('T', 'U')