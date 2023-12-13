import csv
def read_word_list_from_csv(filename):
    word_set = set()    
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for word in row:
                word_set.add(word)    
    return list(word_set)
filename = "energy_bids.csv"  
word_list = read_word_list_from_csv(filename)
with open('eno.txt', 'w') as f:
    f.write(' '.join(word_list))
