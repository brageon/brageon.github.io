import numpy as np
def find_hamiltonian_path(distances):
  visited_cities = np.zeros(len(distances), dtype=bool)
  current_city = 0
  shortest_distance = float('inf')
  shortest_path = None
  total_distance = 0
  path = [current_city]
  while not np.all(visited_cities):
    next_city = np.argmin(distances[current_city] + np.where(visited_cities, np.inf, 0))
    visited_cities[next_city] = True
    current_city = next_city
    path.append(next_city)
    total_distance += distances[current_city] / 100
    total_distance = round(total_distance, 1)
    if total_distance < shortest_distance:
      shortest_distance = total_distance
      shortest_path = path[:]
  return shortest_path, total_distance
distances = np.loadtxt('distances.txt')
shortest_path, shortest_distance = find_hamiltonian_path(distances)
print("Hamiltonian path:", shortest_path)
print("Total distance:", shortest_distance)
