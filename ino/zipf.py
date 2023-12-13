import os, logging
import numpy as np
logger = logging.getLogger('zipf_distribution')
logger.setLevel(logging.INFO)
output_folder = 'zipf'
os.makedirs(output_folder, exist_ok=True)
def zipf_distribution(text_file_path):
    with open(text_file_path) as f:
        text = f.read()
    words = text.split()
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    index = [word for word, count in sorted_word_counts]
    ranks = []
    for i, (word, count) in enumerate(sorted_word_counts):
        ranks.append(i + 1)
    frequencies = []
    for count in word_counts.values():
        frequencies.append(1 / count)
    probabilities = []
    for frequency in frequencies:
        probabilities.append(frequency / np.sum(frequencies))
    return index, ranks, frequencies, probabilities
folder_path = input("Enter folder path: ")
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_name = filename[:-4]
        output_file_path = os.path.join(output_folder, file_name + "w.txt")
        file_handler = logging.FileHandler(output_file_path)
        logger.addHandler(file_handler)
        index, ranks, frequencies, probabilities = zipf_distribution(os.path.join(folder_path, filename))
        logger.info("Words:")
        for inde in index:
            logger.info(inde)
        logger.info("\nRanks:")
        for rank in ranks:
            logger.info(rank)
        logger.info("\nFrequencies:")
        for frequency in frequencies:
            logger.info(frequency)
        logger.info("\nProbabilities:")
        for probability in probabilities:
            logger.info(probability)
        logger.removeHandler(file_handler)


