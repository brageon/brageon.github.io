import re, csv, random
with open('energy_bids.csv', 'r') as file:
    reader = csv.DictReader(file)
    email_column = [row['email'] for row in reader]
word_count, output_email = 0, []
for i in range(1, 7):
    text_file = f"{i}b.txt"
    with open(text_file, 'r') as file:
        synonyms_text = file.read()
    words = [word for row in email_column for word in row.split()]
    word_synonym_map = {}
    for word in words:
        word_synonym_map[word] = random.choice(synonyms_text.split())
    random.shuffle(words)
    for word in words:
        if word in word_synonym_map and word_count < 300:
            output_email.append(word)
            word_count += 1
        elif word_count >= 300:
            break
        else:
            synonym_word = word_synonym_map[word]
            if word_count + len(synonym_word.split()) <= 300:
                output_email.append(synonym_word)
                word_count += len(synonym_word.split())
            else:
                break
    if word_count >= 300:
        break
output_email = ' '.join(output_email)
output_email = re.sub(r'\b[A-Z]+\b', '', output_email)
print("To:", output_email)
