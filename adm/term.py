import numpy as np
def load_word_embeddings(embeddings_path):
    word_to_vector = {}
    with open(embeddings_path, 'r', encoding='utf-8') as file:
        for line in file:
            values = line.split()
            word = values[0]
            vectors = np.asarray(values[1:], dtype='float32')
            word_to_vector[word] = vectors
    return word_to_vector
embeddings_path = 'glove.6B.50d.txt'
word_embeddings = load_word_embeddings(embeddings_path)
word = 'and'
if word in word_embeddings:
    definition = word_embeddings[word]
    print(f"Definition of '{word}': {definition}")
else:
    print(f"No definition found for '{word}'")