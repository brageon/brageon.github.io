import re
matched_words = []
file_path1, file_path2, out_path = 'dan.txt', 'dam.txt', 'eno.txt'
with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
    content1 = file1.read()
    content2 = file2.read()
    words1 = re.findall(r'\b[A-Za-z]+\b', content1)
    words2 = re.findall(r'\b[A-Za-z]+\b', content2)
    for word in words1:
        if word in words2:
            matched_words.append(word)
with open(out_path, 'w') as outfile:
    outfile.write('\n'.join(matched_words))
print(matched_words)
