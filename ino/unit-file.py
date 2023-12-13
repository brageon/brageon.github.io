import re, os, nltk
from google.colab import files
tag_map = {'NNP': 'Z', 'NNPS': 'Z', 'NN': 'Z', 'NNS': 'Z', 'WP': 'Z', 'WPS': 'Z', 'DT': 'Z', 'WDT': 'Z', 'PRP': 'A', 'PRPS': 'A', 'PRP$': 'A', 'EX': 'A', 'POS' : 'A', 'TO': 'A', 'UH': 'J', 'IN': 'J', 'CD': 'J', 'FW': 'J', 'RP': 'J', 'CC': 'J', 'MD' : 'J', 'JJ': 'T', 'JJR': 'T', 'JJS': 'T', 'RB': 'T', 'WRB': 'T', 'RBR': 'T', 'RBS': 'T', 'VBP': 'G', 'VBZ': 'G', 'VBD': 'G', 'VBG': 'G', 'VBN': 'G', 'VB': 'G'}
youn = {'A T G': 15, 'S J Z': 49, 'T Z T': 61, 'J Z Z': 52, 'G Z Z': 52, 'J T T': 32, 'Z A A': 32, 'Z I T': 55, 'Z G I': 45, 'T Z G': 55, 'T G T': 61, 'J Z J': 47, 'A G A': 38, 'Z J Z': 49, 'G A T': 49, 'G J Z': 49, 'A Z T': 49, 'J A T': 49, 'A J T': 49, 'T A Z': 49, 'G G Z': 49, 'A G J': 47, 'G G J': 47, 'J G Z': 47, 'G A G': 47, 'Z A G': 47, 'G J G': 47, 'T Z A': 47, 'Z G G': 47, 'Z G Z': 47}
dict_map = {'Z': 4, 'J': 5, 'G': 6, 'A': 7, 'T': 9}
def translate(text):
  tokens = nltk.word_tokenize(text)
  tag_pairs = nltk.pos_tag(tokens)
  convert = [tag_map.get(tag, tag) for _, tag in tag_pairs]
  word_list = []
  for word in convert:
    if isinstance(word, float):
      continue
    if word in dict_map and isinstance(dict_map[word], str):
      word_list.append(dict_map[word])
    else:
      word_list.append(str(word))
  return word_list
def save_output(output_text, filename):
  with open(filename, 'w') as f:
    f.write(output_text)
text = "nuvi/v32.txt"
with open(text, 'r') as f:
  file_content = f.read()
new = translate(file_content)
men = re.sub(r'[^\w]', ' ', ' '.join(new))
match = []
for pattern in youn.keys():
  match.append(re.search(pattern, men))
output_text = ""
for match in match:
  if match:
    result = match.group()
    output_text += f"Pat: {result}\nSta: {match.start()}\nEnd: {match.end()}\n\n"
filename = "cv32.txt"
save_output(output_text, filename)
files.download(filename)
