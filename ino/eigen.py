import numpy as np
from scipy.sparse.linalg import eigsh
def get_matrix(file_path):
  with open(file_path, 'r') as f:
    matrix = []
    for line in f:
      if line.strip():
        matrix.append([int(x) for x in line.split()])
  return np.array(matrix)
som = get_matrix("mi/m0.txt")
sow = np.pad(som, ((0, 0), (0, 19)))
sov = sow.reshape(6, 120)
sov = sov[:6, :6]
eigenvalues, eigenvectors = eigsh(sov, k=6, which='LM')
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
for i in range(len(eigenvectors)):
  print(eigenvectors[i])
