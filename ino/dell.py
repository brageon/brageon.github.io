def delete_words(file_path, positions):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        new_lines = []
    for line in lines:
        words = line.split()
        new_words = [word for index, word in enumerate(words) if index not in positions]
        new_lines.append(' '.join(new_words) + '\n')
    with open(file_path, 'w') as file:
        file.writelines(new_lines)
    return file
file_path = 'alpha.txt'
positions = [182513, 184351, 217671, 250468, 330558, 360623, 364629]
delete_words(file_path, positions)
