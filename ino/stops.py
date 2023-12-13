import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize
def search_stopwords(file_path):
    stopwords_path = 'dat/english'
    with open(stopwords_path, 'r') as stopwords_file:
       stopwords = stopwords_file.read().splitlines()
    with open(file_path, 'r') as file:
        content = file.read()
    tokenized_text = nltk.word_tokenize(content)
    stop_words = set(stopwords)
    stopwords_found = []
    for i, word in enumerate(tokenized_text):
        if word.lower() in stop_words:
            stopwords_found.append((word, i))
    return stopwords_found
file_path = 'eno.txt'
stopwords_found = search_stopwords(file_path)
print("Stopwords found: ")
with open ('kex.txt', 'w') as f:
    for word, position in stopwords_found:
        xen = f"{position}, "
        f.write(xen)
print("\nCat")
