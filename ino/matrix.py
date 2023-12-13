import re
dict_map = {'Z': 4, 'J': 5, 'G': 6, 'A': 7, 'T': 9}
def remove_non(text):
  return re.findall(r'[A-Z]+', text)
def write_matrix(matrix, filename):
  with open(filename, "w") as f:
    for row in matrix:
      f.write(" ".join([str(item) for item in row]) + "\n")
def translate(text):
  floats = []
  for char in text:
    if char in dict_map:
      floats.append(dict_map[char])
    else:
      floats.append(0)
  return floats
def main():
  with open("nut.txt", "r") as f:
    lines = f.readlines()
  li = [(remove_non(line)) for line in lines]
  kim = [translate(item) for item in li]
  matrix_file = "matrix.txt"
  mat = list(kim)
  write_matrix(mat, matrix_file)
if __name__ == "__main__":
  main()
