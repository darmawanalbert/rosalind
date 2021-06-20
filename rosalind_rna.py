dna_source = input()
rna = ''

for base in dna_source:
    if base == 'T':
        rna += 'U'
    else:
        rna += base

print(rna)
