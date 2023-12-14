'''
Used this before file chunking. I reformat matrix to least row. Making it a square and remove the need for rearranging matrix arithmetic including eigenvectors. I use expected value from every matrix file to check positions in matrix.txt  

awk '{if (NR==2) print $0}' far.txt | wc -w
'''
import os
import numpy as np
def split_file(file_path, output_dir, num_files, lines_per_file, floats_per_line):
  with open(file_path, "r") as f:
    data = f.readlines()
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  matrices = []
  for i in range(0, len(data), lines_per_file):
    matrix = np.array([[int(item) for item in line.split()] for line in data[i:i + lines_per_file]])
    matrices.append(matrix)
  for i in range(num_files):
    output_file_path = os.path.join(output_dir, f"m{i}.txt")
    with open(output_file_path, "w") as f:
      for j in range(lines_per_file):
        for k in range(floats_per_line):
          f.write(str(matrices[i][j][k]))
          if k < floats_per_line - 1:
            f.write(" ")
        f.write("\n")
if __name__ == '__main__':
  file_path, output_dir = "matrix.txt", "mi"
  num_files, lines_per, floats_per = 48, 6, 101
  split_file(file_path, output_dir, num_files, lines_per, floats_per)
