'''ROSALIND bioinformatics scripts that returns that operate on DNA and RNA.'''

from string import maketrans


# Kind of pointless, as it's so simple.
def DNA_to_RNA(dna):
    '''Translates DNA to RNA'''
    return dna.replace('T', 'U')


# Kind of pointless, as it's so simple.
def RNA_to_DNA(rna):
    '''Translates RNA to DNA'''
    return rna.replace('U', 'T')


def ReverseComplementDNA(nucleic_acid):
    '''Returns the reverse complement of a given DNA strand.'''
    nucleotide = 'ATCG'
    complement = 'TAGC'
    transtab = maketrans(nucleotide, complement)

    return nucleic_acid.translate(transtab)[::-1].lstrip()


def ReverseComplementRNA(nucleic_acid):
    '''Returns the reverse complement of a given RNA strand.'''
    nucleotide = 'AUCG'
    complement = 'UAGC'
    transtab = maketrans(nucleotide, complement)

    return nucleic_acid.translate(transtab)[::-1].lstrip()


def HammingDistance(seq1, seq2):
    'Return the Hamming distance between equal-length sequences.'
    if len(seq1) != len(seq2):
        raise ValueError('Undefined for sequences of unequal length.')
    return sum(ch1 != ch2 for ch1, ch2 in zip(seq1, seq2))

'''A ROSALIND bioinformatics script to extract sequence information FASTA format data.'''

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


'''A ROSALIND bioinformatics script to create RNA and DNA to Protein dictionary.'''


def ProteinDictDNA():
    '''Returns a dictionary that translates DNA to Protein.'''
    # Get the raw codon table.
    dna2protein = CodonTableDNA()

    # Convert to dictionary.
    dna_dict = {}
    for translation in dna2protein:
        dna_dict[translation[0]] = translation[1]

    return dna_dict


def ProteinDictRNA():
    '''Returns a dictionary that translates RNA to Protein.'''
    # Get the raw codon table.
    rna2protein = CodonTableRNA()

    # Convert to dictionary.
    rna_dict = {}
    for translation in rna2protein:
        rna_dict[translation[0]] = translation[1]

    return rna_dict


def ProteinWeightDict():
    '''Returns a dictionary that translates Protein to Monoisotopic Mass.'''
    table = '''A   71.03711
	C   103.00919
	D   115.02694
	E   129.04259
	F   147.06841
	G   57.02146
	H   137.05891
	I   113.08406
	K   128.09496
	L   113.08406
	M   131.04049
	N   114.04293
	P   97.05276
	Q   128.05858
	R   156.10111
	S   87.03203
	T   101.04768
	V   99.06841
	W   186.07931
	Y   163.06333'''

    protein_weight_dict = dict()

    for protein in table.split('\n'):
        protein_weight_dict[protein.strip('\t').split()[0]] = float(protein.strip('\t').split()[1])

    return protein_weight_dict


def CodonTableDNA():
    '''Returns a DNA Codon translation list.'''
    table = '''TTT F
	CTT L      
	ATT I      
	GTT V
	TTC F      
	CTC L      
	ATC I      
	GTC V
	TTA L     
	CTA L      
	ATA I      
	GTA V
	TTG L      
	CTG L      
	ATG M      
	GTG V
	TCT S      
	CCT P      
	ACT T      
	GCT A
	TCC S      
	CCC P      
	ACC T      
	GCC A
	TCA S      
	CCA P      
	ACA T      
	GCA A
	TCG S      
	CCG P      
	ACG T      
	GCG A
	TAT Y      
	CAT H      
	AAT N      
	GAT D
	TAC Y      
	CAC H      
	AAC N      
	GAC D
	TAA Stop   
	CAA Q      
	AAA K      
	GAA E
	TAG Stop   
	CAG Q      
	AAG K      
	GAG E
	TGT C      
	CGT R      
	AGT S      
	GGT G
	TGC C      
	CGC R      
	AGC S      
	GGC G
	TGA Stop   
	CGA R      
	AGA R      
	GGA G
	TGG W      
	CGG R      
	AGG R      
	GGG G'''

    table = table.split('\n')
    for index, item in enumerate(table):
        table[index] = item.strip().split()

    return table


def CodonTableRNA():
    '''Returns an RNA Codon translation list.'''
    table = '''UUU F
	UUC F
	UUA L
	UUG L
	UCU S
	UCC S
	UCA S
	UCG S
	UAU Y
	UAC Y
	UAA Stop
	UAG Stop
	UGU C
	UGC C
	UGA Stop
	UGG W
	CUU L
	CUC L
	CUA L
	CUG L
	CCU P
	CCC P
	CCA P
	CCG P
	CAU H
	CAC H
	CAA Q
	CAG Q
	CGU R
	CGC R
	CGA R
	CGG R
	AUU I
	AUC I
	AUA I
	AUG M
	ACU T
	ACC T
	ACA T
	ACG T
	AAU N
	AAC N
	AAA K
	AAG K
	AGU S
	AGC S
	AGA R
	AGG R
	GUU V
	GUC V
	GUA V
	GUG V
	GCU A
	GCC A
	GCA A
	GCG A
	GAU D
	GAC D
	GAA E
	GAG E
	GGU G
	GGC G
	GGA G
	GGG G'''

    table = table.split('\n')
    for index, item in enumerate(table):
        table[index] = item.strip().split()

    return table