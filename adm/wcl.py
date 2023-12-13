import re, random
with open("1c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(IN|CC|MD|RP|FW|TO|UH)\b", content) 
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("1a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("1c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(NN|NNS|NNP|NNPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("2a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("1c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(DT|WDT|WRB|PDT|POS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("3a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("1c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(JJ|JJR|JJS|RB|RBR|RBS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("4a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("1c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(VB|VBD|VBG|VBN|VBP|VBZ)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("5a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("1c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(PRP|PRP$|PRPS|EX|WP|WPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("6a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("2c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(IN|CC|MD|RP|FW|TO|UH)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("1a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("2c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(NN|NNS|NNP|NNPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("2a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("2c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(DT|WDT|WRB|PDT|POS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("3a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("2c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(JJ|JJR|JJS|RB|RBR|RBS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("4a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("2c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(VB|VBD|VBG|VBN|VBP|VBZ)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("5a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("2c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(PRP|PRP$|PRPS|EX|WP|WPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("6a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("3c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(IN|CC|MD|RP|FW|TO|UH)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("1a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("3c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(NN|NNS|NNP|NNPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("2a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("3c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(DT|WDT|WRB|PDT|POS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("3a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("3c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(JJ|JJR|JJS|RB|RBR|RBS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("4a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("3c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(VB|VBD|VBG|VBN|VBP|VBZ)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("5a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("3c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(PRP|PRP$|PRPS|EX|WP|WPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("6a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("4c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(IN|CC|MD|RP|FW|TO|UH)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("1a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("4c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(NN|NNS|NNP|NNPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("2a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("4c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(DT|WDT|WRB|PDT|POS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("3a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("4c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(JJ|JJR|JJS|RB|RBR|RBS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("4a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("4c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(VB|VBD|VBG|VBN|VBP|VBZ)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("5a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("4c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(PRP|PRP$|PRPS|EX|WP|WPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("6a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("5c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(IN|CC|MD|RP|FW|TO|UH)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("1a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("5c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(NN|NNS|NNP|NNPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("2a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("5c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(DT|WDT|WRB|PDT|POS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("3a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("5c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(JJ|JJR|JJS|RB|RBR|RBS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("4a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("5c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(VB|VBD|VBG|VBN|VBP|VBZ)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("5a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("5c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(PRP|PRP$|PRPS|EX|WP|WPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("6a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("6c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(IN|CC|MD|RP|FW|TO|UH)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("1a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("6c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(NN|NNS|NNP|NNPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("2a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("6c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(DT|WDT|WRB|PDT|POS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("3a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("6c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(JJ|JJR|JJS|RB|RBR|RBS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("4a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("6c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(VB|VBD|VBG|VBN|VBP|VBZ)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("5a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("6c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(PRP|PRP$|PRPS|EX|WP|WPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("6a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("7c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(IN|CC|MD|RP|FW|TO|UH)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("1a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("7c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(NN|NNS|NNP|NNPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("2a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("7c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(DT|WDT|WRB|PDT|POS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("3a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("7c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(JJ|JJR|JJS|RB|RBR|RBS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("4a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("7c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(VB|VBD|VBG|VBN|VBP|VBZ)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("5a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("7c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(PRP|PRP$|PRPS|EX|WP|WPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("6a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("8c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(IN|CC|MD|RP|FW|TO|UH)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("1a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("8c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(NN|NNS|NNP|NNPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("2a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("8c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(DT|WDT|WRB|PDT|POS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("3a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("8c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(JJ|JJR|JJS|RB|RBR|RBS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("4a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("8c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(VB|VBD|VBG|VBN|VBP|VBZ)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("5a.txt", "a") as new_file:
    new_file.write("\n" + words)
with open("8c.txt", "r") as file:
    content = file.read()
matches = re.findall(r"\b(\w+)/(PRP|PRP$|PRPS|EX|WP|WPS)\b", content)
words = [m[0] for m in matches] 
pos_tags = [m[1] for m in matches]  
lines = []
for word, pos in zip(words, pos_tags):
    lines.append("{} {}".format(pos, word))
words = ' '.join(lines)
with open("6a.txt", "a") as new_file:
    new_file.write("\n" + words)
def read_word_list(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words
file1 = '1a.txt'
file2 = '2a.txt'
file3 = '3a.txt'
file4 = '4a.txt'
file5 = '5a.txt'
file6 = '6a.txt'
wol1 = read_word_list(file1)
wol2 = read_word_list(file2)
wol3 = read_word_list(file3)
wol4 = read_word_list(file4)
wol5 = read_word_list(file5)
wol6 = read_word_list(file6)
def generate_sentence(wol1, wol2, wol3, wol4, wol5, wol6):
    sentence = '{} {} {} {} {} {}.'.format(
        random.choice(wol1),
        random.choice(wol2),
        random.choice(wol3),
        random.choice(wol4),
        random.choice(wol5),
        random.choice(wol6))
    return sentence
num_sentences = 100
with open('rand.txt', 'a') as file:
    for i in range(num_sentences):
        sentence = generate_sentence(wol1, wol2, wol3, wol4, wol5, wol6)
        file.write(sentence) 
        if (i + 1) % 20 == 0:
            file.write('\n')
        else:
            file.write(' ') 
#Kivy, BeeWare