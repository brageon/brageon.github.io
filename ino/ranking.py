'''
Conceptual analysis. First Z=GAI, J=AWM, G=NVI, A=CPI, T=QRI. Noun is general category. Verb is non-verbal. Interjections is cardinals. Adjective is a description of noun and verb. QRI is motors behind vehicles. Pronoun is active category defined by ownership.  
'''
import numpy as np
import re, nltk, string
from nltk import pos_tag
#nltk.download('averaged_perceptron_tagger')
#nltk.download('punkt')
from collections import Counter
tag_map = {'NNP': 'Z', 'NNPS': 'Z', 'NN': 'Z', 'NNS': 'Z', 'WP': 'Z', 'WPS': 'Z', 'DT': 'Z', 'WDT': 'Z', 'PRP': 'A', 'PRPS': 'A', 'PRP$': 'A', 'EX': 'A', 'POS' : 'A', 'TO': 'A', 'UH': 'J', 'IN': 'J', 'CD': 'J', 'FW': 'J', 'RP': 'J', 'CC': 'J', 'MD' : 'J', 'JJ': 'T', 'JJR': 'T', 'JJS': 'T', 'RB': 'T', 'WRB': 'T', 'RBR': 'T', 'RBS': 'T', 'VBP': 'G', 'VBZ': 'G', 'VBD': 'G', 'VBG': 'G', 'VBN': 'G', 'VB': 'G'}
dict_map = {'Z': 4, 'J': 5, 'G': 6, 'A': 7, 'T': 9}
class BaCl:
  def __init__(self):
    pass
  def translate(self, text):
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
  def split_lines(self, lines, size=400):
    split_lines = []
    for line in lines:
      words = line.split()
      current_line = []
      for word in words:
        current_line.append(word)
        if len(current_line) == size:
          split_lines.append(' '.join(current_line))
          current_line = []
      if current_line:
        split_lines.append(' '.join(current_line))
    return split_lines
  def calc(self, translated):
    words = translated.split(' ')
    line_sum = sum([float(dict_map.get(word, 0)) for word in words])
    count, special_cases = 0, 0
    line = ' '.join(words)
    for i in range(1, len(words)):
      if words[i - 1] == "G" and words[i] == "Z":
        line_sum -= 4
        special_cases += 1
      elif words[i - 1] == "Z" and words[i] == "G":
        line_sum -= 7
        special_cases += 1
      elif words[i - 1] == "T" and words[i] == "J":
        line_sum -= 5
        special_cases += 1
      elif words[i - 1] == "J" and words[i] == "T":
        line_sum -= 9
        special_cases += 1
      elif words[i - 1] == "G" and words[i] == "G":
        line_sum -= 0
        special_cases += 0
      elif words[i - 1] == "Z" and words[i] == "Z":
        line_sum -= 0
        special_cases += 0
      elif words[i - 1] == "A" and words[i] == "A":
        line_sum -= 0
        special_cases += 0
      elif words[i - 1] == "J" and words[i] == "J":
        line_sum -= 0
        special_cases += 0
      elif words[i - 1] == "T" and words[i] == "T":
        line_sum -= 0
        special_cases += 0
      else:
        count += 1
    if count - special_cases > 0:
      ouro = int((line_sum) / (count - special_cases))
    else:
      ouro = dict_map.get(word, 0) if count == 0 else int((line_sum) / (count))
    sums = int(line_sum)
    sun = int(sum([dict_map.get(word, 0) for word in words]))
    return sums, ouro, sun
  def metrics(self, text):
    nwo = sum(len(word) for word in text.split())
    nuw = len(set([''.join([char for char in word if char not in string.punctuation]) for word in text.split()]))
    nse = text.count(' ')
    return nwo, nse, nuw
  def nut_file(self):
    with open("nu.txt", "r") as ce:
      ui = ce.read().splitlines()
    split_lines = self.split_lines(ui)
    count, out, inch, spela = 0, '', [], []
    for line in split_lines:
      genz = self.metrics(line)
      count += 1
      meter = f"{count} {genz}"
      dans = self.translate(line)
      out = ' '.join(dans) + '\n'
      cott = len(re.findall(r"(G Z|Z G|T J|J T)", out))
      inch.append(f"{meter} {out.strip()} {cott}")
    with open("nut.txt", "w") as ce:
      ce.write('\n'.join(inch))
    with open("nut.txt", "r") as ce:
      aik = ce.readlines()
    for ai in aik:
      spel = str(self.calc(ai))
      cv = Counter(ai).most_common(2)[1]
      spela.append(f"{ai} {spel.strip()} {cv}")
    with open("nut1.txt", "w") as ce:
      ce.write('\n'.join(spela))
if __name__ == '__main__':
  baocl = BaCl()
  baocl.nut_file()
