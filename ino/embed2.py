import csv
def calculate_similarity_index(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    common_words = words1.intersection(words2)
    similarity_index = len(common_words) / len(words1)
    return similarity_index
dol1_file = "energy_bids.csv"
energy_bids_file = "a.txt"
similarity_index = calculate_similarity_index(dol1_file, energy_bids_file)
print(f"The word match similarity index is: {similarity_index}")
