import spacy
nlp = spacy.load("en_core_web_sm")
with open("red.txt", "r") as file:
    text = file.read()
    doc = nlp(text)
for sentence in doc.sents:
    for token in sentence:
        print(token.text, token.pos_, token.dep_, token.head.text)