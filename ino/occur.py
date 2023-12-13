import os
from collections import defaultdict
keyword_data = '9'  # 9 6 9 5 4 4 5 7 6 7
def jaccard_similarity(s1, s2):
    s1_set = set(s1.split())
    s2_set = set(s2.split())
    intersection = s1_set & s2_set
    union = s1_set | s2_set
    return len(intersection) / len(union)
def update_best_matches(similarity, substring, position, best_matches, best_similarity):
    if similarity > best_similarity:
        best_similarity = similarity
        best_matches = defaultdict(list)
    if similarity == best_similarity:
        best_matches[similarity].append(substring)
        best_matches[similarity].append(position)
def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f:
        file_content = f.read()
        best_matches = defaultdict(list)
        best_similarity = 0
        for i in range(len(file_content)):
            for j in range(i + 1, len(file_content) + 1):
                substring = file_content[i:j]
                similarity = jaccard_similarity(substring, keyword_data)
                if similarity > best_similarity:
                    break
                update_best_matches(similarity, substring, i, best_matches, best_similarity)
    with open(output_file_path, 'w') as f:
        for similarity, matches in best_matches.items():
            for substring, position in zip(matches[::2], matches[1::2]):
                f.write(f"Similarity: {similarity:.3f}\n")
                f.write(f"Substring: {substring}\n")
                f.write(f"Position: {position}\n")
                f.write("=" * 20 + "\n\n")
input_folder = 'gui'
output_folder = 'zaza2'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename[:-5] + 'd.txt')
        process_file(file_path, output_file_path)


