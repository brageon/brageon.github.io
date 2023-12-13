import os, re
def extract_highest_integer_substrings(filename):
    highest_integer_count = 0
    highest_integer_substrings = ''
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('Substring:'):
                integer_count = 0
                for word in re.findall(r'\d+', line):
                    integer_count += 1
                if integer_count > highest_integer_count:
                    highest_integer_count = integer_count
                    highest_integer_substrings = ''
                if integer_count == highest_integer_count:
                    highest_integer_substrings += line
    return highest_integer_substrings
if __name__ == '__main__':
    for filename in os.listdir('zaza2'):
        if filename.endswith('.txt'):
            highest_integer_substrings = extract_highest_integer_substrings(os.path.join('zaza', filename))
            print(f"File: {filename}")
            print(highest_integer_substrings)
'''
File: v7d.txt
Substring:  4 7 4 4 5 4 5 4 4 5 4 4 4 4 5 5
Substring:  4 7 4 4 5 4 5 4 4 5 4 4 4 4 5 5 
Substring: 4 7 4 4 5 4 5 4 4 5 4 4 4 4 5 5
Substring: 4 7 4 4 5 4 5 4 4 5 4 4 4 4 5 5 

File: v2d.txt
Substring:  5 5 7 4 5 5 4 4 4 4 7
Substring:  5 5 7 4 5 5 4 4 4 4 7 
Substring: 5 5 7 4 5 5 4 4 4 4 7
Substring: 5 5 7 4 5 5 4 4 4 4 7 
Substring:  5 4 5 4 4 5 4 4 5 4 7
Substring:  5 4 5 4 4 5 4 4 5 4 7 
Substring: 5 4 5 4 4 5 4 4 5 4 7
Substring: 5 4 5 4 4 5 4 4 5 4 7 

File: v1d.txt
Substring:  4 4 5 4 5 4 5 4 5 4 5 4 4
Substring:  4 4 5 4 5 4 5 4 5 4 5 4 4 
Substring: 4 4 5 4 5 4 5 4 5 4 5 4 4
Substring: 4 4 5 4 5 4 5 4 5 4 5 4 4 

File: v11d.txt
Substring:  5 4 4 4 4 4 4 5 4 4 5 4 4 5 4 5 5 4 5 4
Substring:  5 4 4 4 4 4 4 5 4 4 5 4 4 5 4 5 5 4 5 4 
Substring: 5 4 4 4 4 4 4 5 4 4 5 4 4 5 4 5 5 4 5 4
Substring: 5 4 4 4 4 4 4 5 4 4 5 4 4 5 4 5 5 4 5 4 

File: v19d.txt
Substring:  5 4 4 5 4 4 4 4 4 5 4 4 4 5 4 4 4
Substring:  5 4 4 5 4 4 4 4 4 5 4 4 4 5 4 4 4 
Substring: 5 4 4 5 4 4 4 4 4 5 4 4 4 5 4 4 4
Substring: 5 4 4 5 4 4 4 4 4 5 4 4 4 5 4 4 4 

File: v27d.txt
Substring:  4 4 5 4 4 4 4 5 4 4 5 4 4 4 5 4 5 7
Substring:  4 4 5 4 4 4 4 5 4 4 5 4 4 4 5 4 5 7 
Substring: 4 4 5 4 4 4 4 5 4 4 5 4 4 4 5 4 5 7
Substring: 4 4 5 4 4 4 4 5 4 4 5 4 4 4 5 4 5 7 

File: v15d.txt
Substring:  4 4 4 5 4 4 4 4 4 7 4 4
Substring:  4 4 4 5 4 4 4 4 4 7 4 4 
Substring: 4 4 4 5 4 4 4 4 4 7 4 4
Substring: 4 4 4 5 4 4 4 4 4 7 4 4 

File: v9d.txt
Substring:  4 5 5 5 7 7 4 7 4 5 4 7
Substring:  4 5 5 5 7 7 4 7 4 5 4 7 
Substring: 4 5 5 5 7 7 4 7 4 5 4 7
Substring: 4 5 5 5 7 7 4 7 4 5 4 7 
Substring:  7 4 5 5 4 4 4 4 4 4 5 7
Substring:  7 4 5 5 4 4 4 4 4 4 5 7 
Substring: 7 4 5 5 4 4 4 4 4 4 5 7
Substring: 7 4 5 5 4 4 4 4 4 4 5 7 

File: v20d.txt
Substring:  4 7 4 4 5 5 5 4 4 5 4 5 4 4 5 5
Substring:  4 7 4 4 5 5 5 4 4 5 4 5 4 4 5 5 
Substring: 4 7 4 4 5 5 5 4 4 5 4 5 4 4 5 5
Substring: 4 7 4 4 5 5 5 4 4 5 4 5 4 4 5 5 

File: v14d.txt
Substring:  5 5 4 4 5 4 5 5 4 4 4 5 4
Substring:  5 5 4 4 5 4 5 5 4 4 4 5 4 
Substring: 5 5 4 4 5 4 5 5 4 4 4 5 4
Substring: 5 5 4 4 5 4 5 5 4 4 4 5 4 
Substring:  4 5 4 5 5 4 4 4 4 5 4 4 4
Substring:  4 5 4 5 5 4 4 4 4 5 4 4 4 
Substring: 4 5 4 5 5 4 4 4 4 5 4 4 4
Substring: 4 5 4 5 5 4 4 4 4 5 4 4 4 

File: v26d.txt
Substring:  5 4 5 7 5 4 5 7 4 5 5 7 4 4 4
Substring:  5 4 5 7 5 4 5 7 4 5 5 7 4 4 4 
Substring: 5 4 5 7 5 4 5 7 4 5 5 7 4 4 4
Substring: 5 4 5 7 5 4 5 7 4 5 5 7 4 4 4 

File: v25d.txt
Substring:  5 5 4 5 4 5 5 4 4 5 4 4 7
Substring:  5 5 4 5 4 5 5 4 4 5 4 4 7 
Substring: 5 5 4 5 4 5 5 4 4 5 4 4 7
Substring: 5 5 4 5 4 5 5 4 4 5 4 4 7 
Substring:  4 4 4 5 4 4 5 5 5 4 4 4 5
Substring:  4 4 4 5 4 4 5 5 5 4 4 4 5 
Substring: 4 4 4 5 4 4 5 5 5 4 4 4 5
Substring: 4 4 4 5 4 4 5 5 5 4 4 4 5 

File: v21d.txt
Substring:  4 4 4 5 5 4 4 4 5 4 4 4 5 4 5 4 4 5 7
Substring:  4 4 4 5 5 4 4 4 5 4 4 4 5 4 5 4 4 5 7 
Substring: 4 4 4 5 5 4 4 4 5 4 4 4 5 4 5 4 4 5 7
Substring: 4 4 4 5 5 4 4 4 5 4 4 4 5 4 5 4 4 5 7 

File: v12d.txt
Substring:  5 4 5 5 4 5 5 4 4 5 4 4 5
Substring:  5 4 5 5 4 5 5 4 4 5 4 4 5 
Substring: 5 4 5 5 4 5 5 4 4 5 4 4 5
Substring: 5 4 5 5 4 5 5 4 4 5 4 4 5 

File: v17d.txt
Substring:  5 5 4 4 4 4 4 4 5 4 4 4 7 4 7
Substring:  5 5 4 4 4 4 4 4 5 4 4 4 7 4 7 
Substring: 5 5 4 4 4 4 4 4 5 4 4 4 7 4 7
Substring: 5 5 4 4 4 4 4 4 5 4 4 4 7 4 7 

File: v5d.txt
Substring:  5 4 4 5 4 5 4 4 5 4 7 5 5 4 4 4
Substring:  5 4 4 5 4 5 4 4 5 4 7 5 5 4 4 4 
Substring: 5 4 4 5 4 5 4 4 5 4 7 5 5 4 4 4
Substring: 5 4 4 5 4 5 4 4 5 4 7 5 5 4 4 4 

File: v28d.txt
Substring:  5 4 4 4 5 4 4 4 4 5 5 7 4 7
Substring:  5 4 4 4 5 4 4 4 4 5 5 7 4 7 
Substring: 5 4 4 4 5 4 4 4 4 5 5 7 4 7
Substring: 5 4 4 4 5 4 4 4 4 5 5 7 4 7 

File: v13d.txt
Substring:  7 4 4 5 4 4 5 4 5 4 4 5 7 4 7 7 4 4 4
Substring:  7 4 4 5 4 4 5 4 5 4 4 5 7 4 7 7 4 4 4 
Substring: 7 4 4 5 4 4 5 4 5 4 4 5 7 4 7 7 4 4 4
Substring: 7 4 4 5 4 4 5 4 5 4 4 5 7 4 7 7 4 4 4 

File: v16d.txt
Substring:  4 4 5 4 5 4 5 4 5 4 5 4 5 4 7
Substring:  4 4 5 4 5 4 5 4 5 4 5 4 5 4 7 
Substring: 4 4 5 4 5 4 5 4 5 4 5 4 5 4 7
Substring: 4 4 5 4 5 4 5 4 5 4 5 4 5 4 7 

File: v3d.txt
Substring:  4 5 5 4 4 5 4 5 4 4 5 4 5 4
Substring:  4 5 5 4 4 5 4 5 4 4 5 4 5 4 
Substring: 4 5 5 4 4 5 4 5 4 4 5 4 5 4
Substring: 4 5 5 4 4 5 4 5 4 4 5 4 5 4 

File: v29d.txt
Substring:  4 4 5 4 4 5 4 4 5 5 4 5 7
Substring:  4 4 5 4 4 5 4 4 5 5 4 5 7 
Substring: 4 4 5 4 4 5 4 4 5 5 4 5 7
Substring: 4 4 5 4 4 5 4 4 5 5 4 5 7 
Substring:  4 4 5 4 4 5 4 4 5 4 4 4 5
Substring:  4 4 5 4 4 5 4 4 5 4 4 4 5 
Substring: 4 4 5 4 4 5 4 4 5 4 4 4 5
Substring: 4 4 5 4 4 5 4 4 5 4 4 4 5 

File: v24d.txt
Substring:  4 5 4 4 5 5 4 4 5 4 4 5 4 5 4 5 7
Substring:  4 5 4 4 5 5 4 4 5 4 4 5 4 5 4 5 7 
Substring: 4 5 4 4 5 5 4 4 5 4 4 5 4 5 4 5 7
Substring: 4 5 4 4 5 5 4 4 5 4 4 5 4 5 4 5 7 

File: v30d.txt
Substring:  5 4 4 5 4 4 5 4 5 4 5 4 4 4
Substring:  5 4 4 5 4 4 5 4 5 4 5 4 4 4 
Substring: 5 4 4 5 4 4 5 4 5 4 5 4 4 4
Substring: 5 4 4 5 4 4 5 4 5 4 5 4 4 4 

File: v10d.txt
Substring:  4 5 4 4 5 4 5 4 4 4 5 4 4
Substring:  4 5 4 4 5 4 5 4 4 4 5 4 4 
Substring: 4 5 4 4 5 4 5 4 4 4 5 4 4
Substring: 4 5 4 4 5 4 5 4 4 4 5 4 4 
Substring:  4 5 4 4 4 5 7 4 5 4 4 5 4
Substring:  4 5 4 4 4 5 7 4 5 4 4 5 4 
Substring: 4 5 4 4 4 5 7 4 5 4 4 5 4
Substring: 4 5 4 4 4 5 7 4 5 4 4 5 4 

File: v8d.txt
Substring:  5 5 4 4 4 5 5 4 4 4 4 4 7
Substring:  5 5 4 4 4 5 5 4 4 4 4 4 7 
Substring: 5 5 4 4 4 5 5 4 4 4 4 4 7
Substring: 5 5 4 4 4 5 5 4 4 4 4 4 7 

File: v31d.txt
Substring:  5 4 5 5 5 4 4 5 4 4 5 7 4 7
Substring:  5 4 5 5 5 4 4 5 4 4 5 7 4 7 
Substring: 5 4 5 5 5 4 4 5 4 4 5 7 4 7
Substring: 5 4 5 5 5 4 4 5 4 4 5 7 4 7 

File: v18d.txt
Substring:  4 5 4 4 5 4 5 4 5 4 4 5
Substring:  4 5 4 4 5 4 5 4 5 4 4 5 
Substring: 4 5 4 4 5 4 5 4 5 4 4 5
Substring: 4 5 4 4 5 4 5 4 5 4 4 5 
Substring:  4 5 4 4 4 5 4 5 4 4 5 5
Substring:  4 5 4 4 4 5 4 5 4 4 5 5 
Substring: 4 5 4 4 4 5 4 5 4 4 5 5
Substring: 4 5 4 4 4 5 4 5 4 4 5 5 
Substring:  7 5 5 4 7 5 7 4 4 7 5 4
Substring:  7 5 5 4 7 5 7 4 4 7 5 4 
Substring: 7 5 5 4 7 5 7 4 4 7 5 4
Substring: 7 5 5 4 7 5 7 4 4 7 5 4 

File: v4d.txt
Substring:  5 5 5 5 4 4 5 4 5 4 4 5 7 5
Substring:  5 5 5 5 4 4 5 4 5 4 4 5 7 5 
Substring: 5 5 5 5 4 4 5 4 5 4 4 5 7 5
Substring: 5 5 5 5 4 4 5 4 5 4 4 5 7 5 

File: v32d.txt
Substring:  4 5 4 4 5 4 5 4 4 5 4 4 7
Substring:  4 5 4 4 5 4 5 4 4 5 4 4 7 
Substring: 4 5 4 4 5 4 5 4 4 5 4 4 7
Substring: 4 5 4 4 5 4 5 4 4 5 4 4 7 

File: v6d.txt
Substring:  4 5 4 4 5 5 4 4 4 4 4 4 4 4 4 5 5 4
Substring:  4 5 4 4 5 5 4 4 4 4 4 4 4 4 4 5 5 4 
Substring: 4 5 4 4 5 5 4 4 4 4 4 4 4 4 4 5 5 4
Substring: 4 5 4 4 5 5 4 4 4 4 4 4 4 4 4 5 5 4 

File: v23d.txt
Substring:  4 4 5 4 5 4 4 5 4 5 4 5 5 7
Substring:  4 4 5 4 5 4 4 5 4 5 4 5 5 7 
Substring: 4 4 5 4 5 4 4 5 4 5 4 5 5 7
Substring: 4 4 5 4 5 4 4 5 4 5 4 5 5 7 
Substring:  4 4 4 5 4 5 4 4 4 5 4 5 4 5
Substring:  4 4 4 5 4 5 4 4 4 5 4 5 4 5 
Substring: 4 4 4 5 4 5 4 4 4 5 4 5 4 5
Substring: 4 4 4 5 4 5 4 4 4 5 4 5 4 5 

File: v22d.txt
Substring:  7 4 5 4 5 5 4 5 4 4 5 4 5 7
Substring:  7 4 5 4 5 5 4 5 4 4 5 4 5 7 
Substring: 7 4 5 4 5 5 4 5 4 4 5 4 5 7
Substring: 7 4 5 4 5 5 4 5 4 4 5 4 5 7 
'''