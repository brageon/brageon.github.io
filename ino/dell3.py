def delete_words(file_path, index_path, output_path):
    with open(file_path, 'r') as file:
        content = file.read()
    with open(index_path, 'r') as index_file:
        indices = [int(index) for index in index_file.read().split(',') if index.strip()]
    words = content.split()
    for index in sorted(indices, reverse=True):
        if index < len(words):
            del words[index]
    modified_content = ' '.join(words)
    with open(output_path, 'w') as output_file:
        output_file.write(modified_content)
file_path, index_path, output_path = 'eno.txt', 'kex.txt', 'dan.txt'
delete_words(file_path, index_path, output_path)
