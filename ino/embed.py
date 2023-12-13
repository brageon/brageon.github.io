from gensim.models import KeyedVectors
filename = "glove.6B.100d.txt"
model = KeyedVectors.load_word2vec_format(filename, binary=False)
sentences = ["and if you're",
    "in test for",
    "I was down",
    "if you're trying",
    "root for game",
    "buy our groceries",]
embeddings = []
for sentence in sentences:
    words = sentence.split()
    embedding = np.zeros(100)
    for word in words:
        if word in model:
            embedding += model[word]
    embedding /= len(words)
    embeddings.append(embedding)
for embedding in embeddings:
    print(embedding)
