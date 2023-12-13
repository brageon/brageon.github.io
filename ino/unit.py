import re, nltk
#nltk.download('averaged_perceptron_tagger')
#nltk.download('punkt')
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
som = ['your', 'groceries', 'groceries', 'and', 'but', 'i', 'think', 'i', 'mean', 'i', 'i', "don't", 'enjoy', 'paying', 'taxes', 'and', "it's", 'hard', 'but', 'um', 'i', 'think', "that's", 'what', 'we', 'have', 'to', 'have', 'to', 'you', 'know', 'have', 'our', 'streets', 'and', 'and', 'have', 'our', 'government', 'and', 'excuse', 'me', 'and', 'have', 'and', 'have', 'the', 'services', 'that', 'we', 'need', 'and', 'we', 'have', 'to', 'pay', 'for', 'them', 'and', 'pay', 'for', 'the', 'employment', 'of', 'the', 'people', 'that', 'run', 'them', 'and', 'and', 'things', 'like', 'that', 'and', 'i', 'think', 'i', 'guess', 'what', 'i', 'feel', 'is', 'that', 'most', 'people', 'um', 'they', "don't", 'like', 'to', 'pay', 'taxes', 'because', 'they', 'feel', 'like', 'well', "there's", 'some', 'people', 'who', "aren't", 'paying', 'their', 'fair', 'share', 'yeah', 'i', 'think', 'yeah', "it's", 'the', 'people', 'that', 'can', 'really', 'influence', 'the', 'government', 'and', 'have', 'all', 'the', 'money', 'to', 'and', 'um', 'that', 'makes', 'you', 'feel', 'bad', 'right', 'and', 'you', 'know', 'when', 'um', 'when', 'last', 'year', 'the', 'the', 'elections', 'were', 'going', 'on', 'the', 'governors', 'election', 'and', 'state', 'and', 'you', 'know', 'i', 'i', "didn't", 'have', 'anything', 'against', 'um', 'Clayton', 'Williams', 'personally', 'or', 'anything', 'but', 'um', 'it', 'was', 'kind', 'of', 'hard', 'for', 'me', 'to', 'think', "here's", 'someone', 'who', 'as', 'wealthy', 'as', 'he', 'is', "didn't", 'have', 'to', 'pay', 'any', 'income', 'tax', 'that', 'he', 'said', 'that', 'year', 'he', 'claimed', 'he', 'had', "didn't", 'have', 'to', 'pay', 'income', 'tax', 'and', 'he', 'thought']
mew = re.sub(r'[^\w]', ' ', ' '.join(som))
new = translate(mew)
print(mew)
for index, word in enumerate(mew.split()):
  print(f"Index: {index}, Word: {word}")
men = re.sub(r'[^\w]', ' ', ' '.join(new))
match = []
for pattern in youn.keys():
  match.append(re.search(pattern, men))
for match in match:
  if match:
    result = match.group()
    print("Pat:", result)
    print("Sta:", match.start())
    print("End:", match.end())
