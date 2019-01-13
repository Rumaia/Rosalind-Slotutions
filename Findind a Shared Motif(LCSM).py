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

def LongestSubstring(string_list):
	'''Extracts all substrings from the first string in a list, and sends longest substring candidates to be checked.'''
	longest = ''
	for start_index in xrange(len(string_list[0])):
		for end_index in xrange(len(string_list[0]), start_index, -1):
			# Break if the length becomes too small, as it will only get smaller.
			if end_index - start_index <= len(longest):
				break
			elif CheckSubstring(string_list[0][start_index:end_index], string_list):
				longest =  string_list[0][start_index:end_index]

	return longest

def CheckSubstring(find_string, string_list):
	'Checks if a given substring appears in all members of a given collection of strings and returns True/False.'
	for string in string_list:
		if (len(string) < len(find_string)) or (find_string not in string):
			return False
	return True


if __name__ == '__main__':
    fasta_list = ReadFASTA('rosalind_lcsm.txt')
    dna = []
    for fasta in fasta_list:
    	dna.append(fasta[1])

    lcsm = LongestSubstring(dna)
    print lcsm
    with open('output_LCSM.txt', 'w') as output_data:
    	output_data.write(lcsm)