import spacy, random
from spacy import displacy
from transformers import pipeline
nlp = spacy.load('en_core_web_sm')
def generate_argument():
    classifier = pipeline("text-classification", model="../tokens")
    subjects, objects, verbs, modal, person, deo = [], [], [], [], [], []
    with open('2a.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  
                words = line.strip().split()
                if len(words) >= 2:
                    subjects.append(words[1])
    with open('4a.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  
                words = line.strip().split()
                if len(words) >= 2:
                    objects.append(words[1])
    with open('5a.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  
                words = line.strip().split()
                if len(words) >= 2:
                    verbs.append(words[1])    
    with open('1a.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  
                words = line.strip().split()
                if len(words) >= 2:
                    modal.append(words[1])
    with open('6a.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  
                words = line.strip().split()
                if len(words) >= 2:
                    person.append(words[1])
    with open('3a.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  
                words = line.strip().split()
                if len(words) >= 2:
                    deo.append(words[1])
    num_arguments = 5
    arguments = []
    for _ in range(num_arguments):
        sub = random.choice(subjects)
        vb = random.choice(verbs)
        ob = random.choice(objects)
        pur = random.choice(person)
        dem = random.choice(deo)
        mod = random.choice(modal)
        argument = f"{dem} {ob} {sub} {pur} {vb} {mod}"
        doc = nlp(argument)
        parsed_argument = ""
        for token in doc:
            parsed_argument += f"{token.text} ({token.dep_}), "
        parsed_argument = parsed_argument.rstrip(", ")
        classification = classifier(argument)[0]
        argument = f"{classification['label']} ({parsed_argument})"
        arguments.append(argument)  
    return arguments
arguments = generate_argument()
for argument in arguments:
    print(argument)