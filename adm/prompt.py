'''
It says string or bytes expected in translate. I will review the logic someday. 
'''
import re, csv, nltk, time, scipy, numpy, socket
import threading, logging, warnings, subprocess
from nlptools.preprocessing.tagging import MLTagger
from sklearn.linear_model import LinearRegression
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
    def __init__(self):
        self.tagger = MLTagger()
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
        words = [str(word) for word in words]
        words = ' '.join(words)
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
def handle_input():
    while True:
        user1 = input("P1: ")
        user2 = input("P2: ")
        user3 = input("P3: ")    
        if user1 == "stop":
            return
        else:
            words = [user1, user2, user3]
    return words
def main():
    words = handle_input()
    lda = LDA()
    sock = lda.connect_to_server()
    while True:
        line, sums, ouro = lda.amrita(words)
        lda.listen_from_server(sock)
if __name__ == '__main__':
    main()
