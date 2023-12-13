import math, time
import numpy as np
def merge_vectors(v1, v2):
  merged_vector = []
  for i in range(len(v1)):
    merged_vector.append(np.mean([v1[i], v2[i]]))
  return merged_vector
def mean_squared_error(a, b):
  return np.mean(np.square(a - b))
def error_rate(sequence1, sequence2):
  num_errors = 0
  for i in range(len(sequence1)):
    if sequence1[i] != sequence2[i]:
      num_errors += 1
  error_rate = num_errors / len(sequence1)
  return error_rate
max_iterations = 10000
error_threshold = 0.4
x = np.loadtxt("cab.txt")
y = np.loadtxt("cab1.txt")
x[np.where(x < 4)] = 3
y[np.where(y < 4)] = 3
np.savetxt("cab.txt", x)
np.savetxt("cab1.txt", y)
x_norm = x / np.linalg.norm(x)
y_norm = y / np.linalg.norm(y)
yaw = np.dot(x_norm, y_norm)
war = (1 / yaw) + 1
exponent = (1 - x * y) / (2 * np.log(x) + 2 * np.log(y))
A = np.round(1 / ((x * y) ** exponent) / war, 1)
start_time = time.time()
threshold_reached = False
while not threshold_reached:
  solution_found = False
  for _ in range(max_iterations):
    C = np.random.randint(4, 10, size=10)
    Co = [7, 5, 6, 6, 5, 4, 4, 4, 4, 5]
    D = merge_vectors(A, C)
    mse = mean_squared_error(C, np.array([Co]))
    if mse <= 2:
      end_time = time.time()
      elapsed_time = end_time - start_time
      R = error_rate(C, Co)
      if R <= error_threshold:
        print("Expected: ", ' '.join(map(str, C)).strip())
        print("Mean squared error: ", mse)
        print("Elapsed time:", elapsed_time, "seconds")
        print("Error rate:", R)
        solution_found = True
        threshold_reached = True
        break
  if not solution_found:
    print("No solution found within the maximum number of iterations.")
    break
