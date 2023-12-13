import os, re
def count_lines_with_pattern(filename, pattern):
    with open(filename, 'r') as f:
        lines = f.readlines()
    pattern = re.compile(pattern)
    count = 0
    total_lines = len(lines)
    for line in lines:
        if pattern.search(line):
            count += 1
    average_occurrences = count / total_lines
    return average_occurrences
pattern = r'9'
for filename in os.listdir('zaza'):
    if filename.endswith('.txt'):
        average_occurrences = 1 / count_lines_with_pattern(os.path.join('zaza', filename), pattern)
        print(f"File: {filename}")
        print(f"Average occurrences of '{pattern}': {average_occurrences}")


