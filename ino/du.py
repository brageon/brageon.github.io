import nltk
#nltk.download('punkt')
def search_duplicates(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    tokenized_text = nltk.word_tokenize(content)
    duplicates_found = []
    seen_words = set()
    for i, word in enumerate(tokenized_text):
        word = word.lower()
        if word in seen_words:
            duplicates_found.append((word, i))
        else:
            seen_words.add(word)
    return duplicates_found
file_path = 'eno.txt'
duplicates_found = search_duplicates(file_path)
print("Duplicates found: ")
with open('kex.txt', 'w') as f:
    for word, position in duplicates_found:
        xen = f"{position}, "
        f.write(xen)
#print("\nCat")
