from itertools import permutations


def factorial(n):
    '''Returns the value of n!'''
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


with open('rosalind_perm.txt') as input_data:
    perm_set = range(1, int(input_data.read()) + 1)

# Create a list containing ordered lists of all permutations.
perm_list = map(list, list(permutations(perm_set)))

with open('output_PERM.txt', 'w') as output_data:
    # Write the total number of permutations, n!
    output_data.write(str(factorial(len(perm_set))))

    # Write the permuations in the desired format.
    for permutation in perm_list:
        output_data.write('\n' + ' '.join(map(str, permutation)))