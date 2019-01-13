with open('rosalind_subs.txt') as input_data:
	s,t = input_data.readlines()
	s = s.rstrip()
	t = t.rstrip()

locations = []
for i in range(0, len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        locations.append(str(i+1))

print ' '.join(locations)
with open('output_SUBS.txt', 'w') as output_data:
	output_data.write(' '.join(locations))