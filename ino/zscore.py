'''
Use this if you want to compute Z-scores and bruteforce with custom error rate.
'''
import re
import numpy as np
def phi(distance):
  return np.exp(-distance**2)
matrix = np.loadtxt("mi/m0.txt")
x = np.linspace(matrix[:, 0].min(), matrix[:, 0].max(), 6)
y = np.linspace(matrix[:, 1].min(), matrix[:, 1].max(), 6)
distances = np.sqrt((matrix[:, 0] - x)**2 + ((matrix[:, 1] - y)**2))
weights = phi(distances)
mean_values = []
for i in range(len(x)):
  for j in range(len(y)):
    interpolated_value = np.dot(i, j, weights)
    mean_values.append(interpolated_value)
mu = int(str(mean_values[-1:]).strip("[]")) // 10
def generate_elements(n, mean, values):
  elements = []
  for i in range(n):
    element = np.random.normal(mean)
    elements.append(element)
  return elements
def main():
  n, mean = 10, mu
  values = (4, 5, 6, 7, 9)
  array = generate_elements(n, mean, values)
  with open("cab.txt", "w") as f:
    for element in array:
      #fm_element = "{:.2f}".format(element)
      f.write(str(element) + " ")
  input_matrix = np.loadtxt("cab.txt")
  mean = np.mean(input_matrix)
  std = np.std(input_matrix)
  z_score_matrix = (input_matrix - mean) / std
  with open("cab1.txt", "w") as f:
    for element in z_score_matrix:
      #fm_element = "{:.2f}".format(element)
      f.write(str(element) + " ")
if __name__ == '__main__':
  main()
