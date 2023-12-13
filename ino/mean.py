import numpy as np
def get_matrix(file_path):
  with open(file_path, 'r') as f:
    matrix = []
    for line in f:
      if line.strip():
        matrix.append([int(x) for x in line.split()])
  return np.array(matrix)
eigenvalues = np.array([-5.08049655, -2.93075454, 0.32409671, 4.24236032, 5.2581197, 37.18667436])
eigenvectors = np.array([
[-0.23377881, 0.57420051, 0.11835457, 0.54074339, 0.27983821, -0.48054199],
[ 0.49597483, -0.29344959, -0.65405971, 0.22650856, 0.16553228, -0.40174014],
[ 0.46143234, 0.17584258, 0.31625819, -0.02806294, -0.71305056, -0.38329064],
[-0.01040397, 0.3910745, -0.191658, -0.80056789, 0.22232646, -0.34623937],
[-0.69667317, -0.31554524, -0.26649075, -0.03205039, -0.43443469, -0.39280994],
[ 0.03122324, -0.54840901, 0.59197022, -0.11647641, 0.38429934, -0.43196203] ])
eigenvectors = eigenvectors / np.linalg.norm(eigenvectors, axis=1, keepdims=True)
dot_products = np.dot(eigenvalues, eigenvectors.transpose())
max_index = np.argmax(dot_products)
print(max_index)
