import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
output = ['eyeball', 'hallowedly', 'Hallowday', 'our', 'cineplasty', 'teroxide']
definitions1 = ['teroxide is primarily used in specialized applications such as glasses, augmented reality devices, night vision technology, and transparent ceramics.']
definitions2 = ['surgical fitting of a lever to a muscle in an amputation stump to facilitate the operation of an artificial hand.']
embeddings_path = 'glove.6B.50d.txt'
embeddings_index = {}
with open(embeddings_path, encoding='utf-8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs
def calculate_similarity(terms1, terms2):
    embeddings1 = [embeddings_index[word] for word in terms1 if word in embeddings_index and not np.isnan(embeddings_index[word]).any()]
    embeddings2 = [embeddings_index[word] for word in terms2 if word in embeddings_index and not np.isnan(embeddings_index[word]).any()]
    if len(embeddings1) == 0 or len(embeddings2) == 0:
        return 0.0
    avg_embedding1 = np.mean(embeddings1, axis=0)
    avg_embedding2 = np.mean(embeddings2, axis=0)
    avg_embedding1 = avg_embedding1.reshape(1, -1)
    avg_embedding2 = avg_embedding2.reshape(1, -1)
    similarity_1_to_2 = cosine_similarity(avg_embedding1, avg_embedding2)[0][0]
    similarity_2_to_1 = cosine_similarity(avg_embedding2, avg_embedding1)[0][0]
    if abs(similarity_1_to_2 - similarity_2_to_1) < 0.0001: 
        return similarity_1_to_2
    elif similarity_1_to_2 > similarity_2_to_1:
        return similarity_1_to_2
    else:
        return similarity_2_to_1
similarity1 = calculate_similarity(output, definitions1)
similarity2 = calculate_similarity(output, definitions2)
if similarity1 > similarity2:
    sentence_meaning = definitions1
elif similarity1 < similarity2:
    sentence_meaning = definitions2
else:
    sentence_meaning = output
print("Most Similar Sentence Meaning:")
print(' '.join(sentence_meaning))