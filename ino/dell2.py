def extract_unique_words(file_path):
    unique_words = set()
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            unique_words.update(words)
    return unique_words
file_path = 'alpha.txt'
unique_words = extract_unique_words(file_path)
with open('alpha2.txt', 'w') as file:
    file.writelines(' '.join(unique_words))
