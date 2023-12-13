import numpy as np
def read_matrix_from_file(file_path):
  with open(file_path, "r") as f:
    lines = f.readlines()
    matrix = []
    for line in lines:
      row = [float(item) for item in line.split()]
      matrix.append(row)
  return np.array(matrix)
def calculate_row_sums(matrix):
  row_sums = np.sum(matrix, axis=1)
  return row_sums
matrix = read_matrix_from_file("mi/m0.txt")
row_sums = calculate_row_sums(matrix)
mix = np.sum(row_sums)
col_mean = int(mix / 101)
print(row_sums)
print(col_mean)
print(mix)
