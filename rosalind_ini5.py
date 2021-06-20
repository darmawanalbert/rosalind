even_lines = []

with open('rosalind_ini5.txt') as file_object:
    all_lines = file_object.readlines()
    for i in range(len(all_lines)):
        if i % 2 == 1:
            even_lines.append(all_lines[i])

with open('rosalind_ini5_output.txt', 'w') as file_object:
    for line in even_lines:
        file_object.write(line)
