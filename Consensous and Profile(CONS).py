from numpy import zeros
import urllib
import contextlib


def ReadFASTA(data_location):
    '''Determines the data type of the FASTA format data and passes the appropriate information to be parsed.'''

    # If given a list, return fasta information from all items in the list.
    if type(data_location) == list:
        fasta_list = []
        for location in data_location:
            fasta_list += ReadFASTA(location)
        return fasta_list

    # Check for a text file, return fasta info from the text file.
    if data_location[-4:] == '.txt':
        with open(data_location) as f:
            return ParseFASTA(f)

    # Check for a website, return fasta info from the website.
    elif data_location[0:4] == 'http':
        with contextlib.closing(urllib.urlopen(data_location)) as f:
            return ParseFASTA(f)


def ParseFASTA(f):
    '''Extracts the Sequence Name and Nucleotide/Peptide Sequence from the a FASTA format file or website.'''
    fasta_list = []
    for line in f:

        # If the line starts with '>' we've hit a new DNA strand, so append the old one and create the new one.
        if line[0] == '>':

            # Using try/except because intially there will be no current DNA strand to append.
            try:
                fasta_list.append(current_dna)
            except UnboundLocalError:
                pass

            current_dna = [line.lstrip('>').rstrip('\n'), '']

        # Otherwise, append the current DNA line to the current DNA
        else:
            current_dna[1] += line.rstrip('\n')

    # Append the final DNA strand after reading all the lines.
    fasta_list.append(current_dna)

    return fasta_list

# Data is in FASTA form
dna_list = ReadFASTA('rosalind_cons.txt')

# Setup an array and count into the array
M = zeros((4,len(dna_list[0][1])), dtype = int)
snp_dict = {'A':0, 'C':1, 'G':2, 'T':3}
for dna in dna_list:
    for index, snp in enumerate(dna[1]):
        M[snp_dict[snp]][index] += 1

# Determine the consensus string
consensus = ''
to_snp = {0:'A', 1:'C', 2:'G', 3:'T'}
for i in range(0,len(dna_list[0][1])):
    maxval = [-1,-1]
    for j in range(0,4):
        if maxval[1] < M[j][i]:
            maxval = [j, M[j][i]]
    consensus += to_snp[maxval[0]]

# Format the count properly
consensus = [consensus, 'A:', 'C:', 'G:', 'T:']
for index, col in enumerate(M):
    for val in col:
        consensus[index+1] += ' '+str(val)

# Print and write the output
print '\n'.join(consensus)
with open('output_CONS.txt', 'w') as output_data:
    output_data.write('\n'.join(consensus))