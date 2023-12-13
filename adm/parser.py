import nltk
import numpy as np 
nltk.data.path.append("~/nltk_data")
from nltk.corpus import words
all_words = words.words('en')
pos_tags = ['WRB', 'VBD', 'PRP', 'RB', 'DT', 'IN', 'NN', '.']
adverbs = [word for word in all_words if nltk.pos_tag([word])[0][1] in pos_tags and nltk.pos_tag([word])\
[0][1].startswith('WRB, EX, CC, MD')]
verbs = [word for word in all_words if nltk.pos_tag([word])[0][1] in pos_tags and nltk.pos_tag([word])\
[0][1] == 'VB, VBD, VBG, VBN, VBP, VBZ']
pronouns = [word for word in all_words if nltk.pos_tag([word])[0][1] in pos_tags and nltk.pos_tag([word])\
[0][1] == 'PRP, PRP$, PRPS']
adjective = [word for word in all_words if nltk.pos_tag([word])[0][1] in pos_tags and nltk.pos_tag([word])\
[0][1] == 'JJ, JJR, JJS, RBR, RBS, RB']
article = [word for word in all_words if nltk.pos_tag([word])[0][1] in pos_tags and nltk.pos_tag([word])\
[0][1] == 'UH, DT, PDT, WDT']
prepositions = [word for word in all_words if nltk.pos_tag([word])[0][1] == 'IN, TO, FW, RP']
nouns = [word for word in all_words if nltk.pos_tag([word])[0][1] in pos_tags and nltk.pos_tag([word])\
[0][1] == 'NN, NNP, NNS, NNPS, POS']
num_sentences = 200
sentences_per_line = 10
output_text = ""
for i in range(num_sentences):
    sentence = np.random.choice(adverbs) + " "
sentence += np.random.choice(verbs) + " "
sentence += np.random.choice(pronouns) + " "
sentence += np.random.choice(adjective) + " "
sentence += np.random.choice(article) + " "
sentence += np.random.choice(prepositions) + " "
sentence += np.random.choice(nouns) + " "
sentence += np.random.choice(all_words)
sentence += "\n" if (i+1) % sentences_per_line == 0 else " "
output_text += sentence
with open("parse.txt", "w") as file:
    file.write(output_text)