import random
import numpy as np
def generate_sentences(file_path):
  with open(file_path, 'r') as f:
    text = f.read()
  sentences = []
  for i in range(6):
    random_value = np.random.rand()
    random_index = int(random_value * len(text.split(",")))
    random_word = text.split(",")[random_index]
    sentence = ",".join([random_word])
    sentence += ","
    sentences.append(sentence)
  random.shuffle(sentences)
  for sentence in sentences:
    print(sentence)
if __name__ == "__main__":
  file_path = "genc.txt"
  generate_sentences(file_path)
