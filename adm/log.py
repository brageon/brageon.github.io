import re, numpy, pandas, collections
dict_map = {"n": 0.0, "Z": 0.3, "S": 0.3, "A": 0.7, "G": 0.7, "J": 0.5, "T": 1.5}
line, sums, means = [], [], []
with open('res.log', 'r') as file:
    data = [line.strip()[1:-1].split(', ') for line in file]
    for tup in data:
        line.append(re.sub(r"[()\',]", "", tup[0]))
        sums.append(re.sub(r"[()\',]", "", tup[1]))
        means.append(re.sub(r"[()\',]", "", tup[2]))
line_arr = numpy.array(line)
line_df = pandas.DataFrame(line_arr, columns=['user']) 
line_df.to_csv('line.csv', index=False)
sums_arr = numpy.array(sums, dtype=float)
means_arr = numpy.array(means, dtype=float)
def diff(a, b):
    return abs(a - b)
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
print(chosen_values)
numu = len(chosen_values) // 2
names = [f'P{i+1}' for i in range(numu)]
split_values = numpy.array(chosen_values).reshape(-1, numu)
df = pandas.DataFrame(split_values, columns=[names])
df.to_csv('lisp.csv', index=False)