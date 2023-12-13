import os, re, nltk, string
import numpy as np
from nltk import pos_tag
from collections import Counter
tag_map = {'NNP': 'Z', 'NNPS': 'Z', 'NN': 'Z', 'NNS': 'Z', 'WP': 'Z', 'WPS': 'Z', 'DT': 'Z', 'WDT': 'Z', 'PRP': 'A', 'PRPS': 'A', 'PRP$': 'A', 'EX': 'A', 'POS' : 'A', 'TO': 'A', 'UH': 'J', 'IN': 'J', 'CD': 'J', 'FW': 'J', 'RP': 'J', 'CC': 'J', 'MD' : 'J', 'JJ': 'T', 'JJR': 'T', 'JJS': 'T', 'RB': 'T', 'WRB': 'T', 'RBR': 'T', 'RBS': 'T', 'VBP': 'G', 'VBZ': 'G', 'VBD': 'G', 'VBG': 'G', 'VBN': 'G', 'VB': 'G'}
dict_map = {'Z': 4, 'J': 5, 'G': 6, 'A': 7, 'T': 9}
def translate_words(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    words = re.findall(r'\w+', text.lower())
    tagged_words = pos_tag(words)
    integer_translations = []
    for word, tag in tagged_words:
        if tag in tag_map:
            integer = dict_map[tag_map[tag]]
        else:
            integer = 0
        integer_translations.append(integer)
    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, integer_translations)))
input_folder = 'nuvi'
output_folder = 'gui'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename[:-4] + 'u.txt')
        translate_words(input_file, output_file)
