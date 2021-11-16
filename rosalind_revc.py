def base_complement(base):
    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'A'
    elif base == 'G':
        return 'C'
    else:
        return 'G'

dna_string = input()
reverse_dna_string = ''.join([base_complement(base) for base in dna_string[::-1]])
print(reverse_dna_string)
