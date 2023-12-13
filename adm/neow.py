import re, nltk
tagged_lines, li = [], []
with open('1b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        tagged_lines.append(tagged)
for line in tagged_lines:
    tagged_string = ' '.join([f"{word}/{tag}" 
    for word, tag in line])
    li.append(tagged_string)
with open('1c.txt', 'a') as file:
    file.write('\n'.join(li))
tagged_lines, li = [], []
with open('2b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        tagged_lines.append(tagged)
for line in tagged_lines:
    tagged_string = ' '.join([f"{word}/{tag}" 
    for word, tag in line])
    li.append(tagged_string)
with open('2c.txt', 'a') as file:
    file.write('\n'.join(li))
tagged_lines, li = [], []
with open('3b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        tagged_lines.append(tagged)
for line in tagged_lines:
    tagged_string = ' '.join([f"{word}/{tag}" 
    for word, tag in line])
    li.append(tagged_string)
with open('3c.txt', 'a') as file:
    file.write('\n'.join(li))
tagged_lines, li = [], []
with open('4b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        tagged_lines.append(tagged)
for line in tagged_lines:
    tagged_string = ' '.join([f"{word}/{tag}" 
    for word, tag in line])
    li.append(tagged_string)
with open('4c.txt', 'a') as file:
    file.write('\n'.join(li))
tagged_lines, li = [], []
with open('5b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        tagged_lines.append(tagged)
for line in tagged_lines:
    tagged_string = ' '.join([f"{word}/{tag}" 
    for word, tag in line])
    li.append(tagged_string)
with open('5c.txt', 'a') as file:
    file.write('\n'.join(li))
tagged_lines, li = [], []
with open('6b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        tagged_lines.append(tagged)
for line in tagged_lines:
    tagged_string = ' '.join([f"{word}/{tag}" 
    for word, tag in line])
    li.append(tagged_string)
with open('6c.txt', 'a') as file:
    file.write('\n'.join(li))
tagged_lines, li = [], []
with open('7b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        tagged_lines.append(tagged)
for line in tagged_lines:
    tagged_string = ' '.join([f"{word}/{tag}" 
    for word, tag in line])
    li.append(tagged_string)
with open('7c.txt', 'a') as file:
    file.write('\n'.join(li))
tagged_lines, li = [], []
with open('8b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        tagged_lines.append(tagged)
for line in tagged_lines:
    tagged_string = ' '.join([f"{word}/{tag}" 
    for word, tag in line])
    li.append(tagged_string)
with open('8c.txt', 'a') as file:
    file.write('\n'.join(li))