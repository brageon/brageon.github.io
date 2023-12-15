'''
Run socks.py inside another tab before this. Log.py is for old version. I have nlptools on PC.  

nc -l 1234 works if socks.py will not. 
'''
import re, nltk, logging, socket, threading, warnings
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.tag import DefaultTagger
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
tag_map = {'NNP': 'Z', 'NNPS': 'Z', 'NN': 'Z', 'NNS': 'Z', 'PRP': 'A', 'WP': 'Z', 'WPS': 'Z', 'UH': 'S', 'DT': 'S', 'WDT': 'S', 'IN': 'J', 'CD': 'J', 'FW': 'J',
'JJ': 'T', 'JJR': 'T', 'JJS': 'T', 'RB': 'T', 'RBR': 'T', 'RBS': 'T', 'VBP': 'G', 'VBZ': 'G', 'VBD': 'G', 'VBG': 'G', 'VBN': 'G', 'VB': 'G',
'RP': 'A', 'EX': 'A', 'CC': 'A', 'WRB': 'A', 'MD': 'A', '.': 'n'}
dict_map = {'Z': 4, 'J': 5, 'G': 6, 'A': 7, 'T': 9}
logging.basicConfig(filename='res.log', level=logging.INFO, format='%(message)s')
warnings.filterwarnings("ignore", category=DeprecationWarning)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logger = logging.getLogger()
lock = threading.Lock()
server = ('localhost', 1234)
class LDA:
    def __init__(self, tags):
        self.tagger = DefaultTagger(tags)
    def translate(self, text):
        tokens = nltk.word_tokenize(text)
        tag_pairs = nltk.pos_tag(tokens)
        convert = [tag_map.get(tag, tag) for _, tag in tag_pairs]
        word_list = []
        previous_word = None
        word_count = {}
        for word in convert:
            if isinstance(word, float):
                continue
            if word in dict_map and isinstance(dict_map[word], str):
                if word == previous_word:
                    word_count[previous_word] += 1
                else:
                    word_list.append(dict_map[word])
                    word_count[word] = 1
                previous_word = word
            else:
                word_list.append(str(word))
        return word_list
    def amrita(self, words):
        prev_letter = None
        words = self.translate(words)
        words = words.split(' ')
        line_sum = sum([float(dict_map.get(word, 0)) for word in words])
        count, special_cases = 0, 0
        line = ' '.join(words)
        for i in range(1, len(words)):
            if word == "n":
                pass
            elif words[i - 1] == "G" and words[i] == "Z":
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
                line_sum += self.dict_map[word]
                count += 1
            prev_letter = word
        line = ','.join(words)
        sums = f"{round(line_sum, 2)}"
        if count - special_cases > 0:
            ouiro = f"{round((line_sum) / (count - special_cases), 1)}"
        elif count == 0:
            ouiro = f"{round((line_sum) / 1, 1)}"
        else:
            ouiro = f"{round((line_sum) / (count), 1)}"
        return line, sums, ouro
    def connect_to_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server)
        logger.info("Connected to server")
        return sock
    def listen_from_server(self, sock):
        while True:
            data = sock.recv(1024)
            logger.info("Received data: %s" % data)
            if not data:
                break
    def process_log(data):
        line, sums, means = [], [], []
        for tup in data:
            line.append(re.sub(r"[()\',]", "", tup[0]))
            sums.append(re.sub(r"[()\',]", "", tup[1]))
            means.append(re.sub(r"[()\',]", "", tup[2]))
        line_arr = numpy.array(line)
        line_df = pandas.DataFrame(line_arr, columns=['user'])
        line_df.to_csv('line.csv', index=False)
        sums_arr = numpy.array(sums, dtype=float)
        means_arr = numpy.array(means, dtype=float)
        chosen_values = []
        for item, s, m in zip(line_arr, sums_arr, means_arr):
            frequencies = {}
        for char in item:
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1
        closest_mean = float('inf')
        closest_value = ''
        for char in item:
            mean_difference = diff(dict_map[char], m)
            if mean_difference < closest_mean:
                closest_mean = mean_difference
                closest_value = char
        chosen_values.append(closest_value)
        numu = len(chosen_values) // 2
        names = [f'P{i + 1}' for i in range(numu)]
        split_values = numpy.array(chosen_values).reshape(-1, numu)
        df = pandas.DataFrame(split_values, columns=names)
        df.to_csv('lisp.csv', index=False)
        with open('lisp.csv', 'a') as f:
            f.write(line + "," + sums + "," + ouro + "\n")
    def log_handler():
        while True:
            with open("res.log", "r") as f:
                for line in f:
                    logging.info(line.strip())
                t = threading.Thread(target=log_handler)
                t.daemon = True  # exit with the main thread
                t.start()
    def generate_prompts(self, words):
        tokenized_words = [word_tokenize(sentence) for sentence in words]
        stemmer = WordNetLemmatizer()
        stemmed_words = []
        for sentence in tokenized_words:
            stemmed_sentence = []
            for word in sentence:
                stemmed_sentence.append(stemmer.lemmatize(word))
            stemmed_words.append(stemmed_sentence)
            prompts = []
        for i in range(len(stemmed_words)):
            prompt = ""
        for word in stemmed_words[i]:
            prompt += word + " "
        prompts.append(prompt)
        return prompts
    def log_output(self, output):
        logging.info(output)
        with open('output.log', 'a') as f:
            f.write(output + '\n')
    def handle_input(self):
        while True:
            user1 = input("P1: ")
            user2 = input("P2: ")
            user3 = input("P3: ")
            if user1 == "stop":
                return
            else:
                self.log_output(f"P1: {user1}; P2: {user2}; P3: {user3}")
                words = [user1, user2, user3]
                prompts = self.generate_prompts(words)
                for prompt in prompts:
                    print(prompt)
def main():
    while True:
        lda = LDA(tag_map)
        words = lda.handle_input()
        sock = lda.connect_to_server()
        while True:
            line, sums, ouro = lda.amrita(words)
            lda.listen_from_server(sock)
            lda.log_output(f"line: {line}; sums: {sums}; ouro: {ouiro}")
            # process_log(f"line: {line}; sums: {sums}; ouro: {ouiro}")
if __name__ == '__main__':
    main()
