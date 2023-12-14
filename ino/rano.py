import re, random
def generate_sentences(file_path):
  with open(file_path, 'r') as f:
    text = f.read()
  sentences = []
  for i in range(6):
    words = random.sample(text.split(","), 1)
    sentence = ",".join(words)
    sentence += ","
    sentences.append(sentence)
  random.shuffle(sentences)
  for sentence in sentences:
    print(sentence)
def count_permutations(file_path):
  with open(file_path, 'r') as f:
    sentences = f.read()
    units = re.split('[,\s]+', sentences)
    permutation_count = 0
    subset_count = 0
    while subset_count < len(units):
      unique_units = set()
      for _ in range(5):
        random_index = random.randrange(len(units))
        unique_units.add(units.pop(random_index))
      subset_count += 1
      permutation_count += len(list(unique_units))
  return permutation_count
if __name__ == "__main__":
  file_path = "genc.txt"
  generate_sentences(file_path)
  permutation_count = count_permutations(file_path)
  #print(f"Total of 5 sentences: {permutation_count}")
