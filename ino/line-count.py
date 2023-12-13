def count_words(line):
    words = line.split()
    return len(words)
filename = "cab"
with open(filename, "r") as file:
    for line_num, line in enumerate(file, 1):
        word_count = count_words(line)
        print(f"Line {line_num} - Word count: {word_count}")
