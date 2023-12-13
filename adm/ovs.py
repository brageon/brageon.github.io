import nltk
def parse_sentence_to_ovs(sentence):
    words = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)
    ovs_syntax = []
    for word, tag in pos_tags:
        if tag.startswith('V'):
            ovs_syntax.append(word)
        elif tag.startswith('N'):
            ovs_syntax.insert(0, word)
        else:
            ovs_syntax.append(word)
    return ' '.join(ovs_syntax)
sentence = "eyeball hallowedly Hallowday our cineplasty teroxide"
ovs_sentence = parse_sentence_to_ovs(sentence)
def convert_to_ovs_syntax(phrase):
    words = phrase.split()
    ovs_phrase = f"{words[0]} {words[4]} {words[5]} {words[1]} {words[3]}"
    return ovs_phrase
ovs_phrase_3 = convert_to_ovs_syntax(ovs_sentence)
print(ovs_sentence)
print(ovs_phrase_3)