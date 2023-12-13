import spacy
nlp = spacy.load("en_core_web_sm")
with open("sw2001.txt", "r") as file:
    text = file.read()
doc = nlp(text)
for entity in doc.ents:
    print(entity.text, entity.label_)
