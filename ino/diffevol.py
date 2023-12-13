import numpy as np
import matplotlib.pyplot as plt
def differential_evolution(population, f, max_iter, F, CR):
  best_solution = population[0]
  best_fitness = f(best_solution)
  fitness_history = []
  second_derivatives = []
  local_optima_positions = []
  for iter in range(max_iter):
    for i in range(len(population)):
      v = population[i]
      r1, r2, r3 = np.random.choice(len(population), size=3, replace=False)
      x1, x2, x3 = population[r1], population[r2], population[r3]
      donor_vector = x1 + F * (x2 - x3)
      trial_vector = np.copy(v)
      for j in range(len(v)):
        if np.random.rand() < CR or j == np.random.randint(0, len(v)):
          trial_vector[j] = donor_vector[j]
          trial_fitness = f(trial_vector)
          if trial_fitness < best_fitness:
            best_solution = trial_vector
            best_fitness = trial_fitness
            second_derivative = 0
            for j in range(len(v)):
              second_derivative += 2 * (trial_vector[j] - v[j])**3
              fitness_history.append(best_fitness)
              second_derivatives.append(second_derivative)
            if len(second_derivatives) > 2 and second_derivatives[-1] < 0 and second_derivatives[-2] > 0:
              local_optima_positions.append(iter)
  return best_solution, fitness_history, second_derivatives, local_optima_positions
def f(x):
    return np.sum(x**2)
max_iter, F, CR = 100, 0.5, 0.8
matrix = np.loadtxt('mi/m0.txt', dtype=int)
population = matrix.copy()
best_solution, fitness_history, second_derivatives, local_optima_positions = differential_evolution(
  population, f, max_iter, F, CR)
print("Best solution:", best_solution)
print("Best fitness:", f(best_solution))
print("Local optima positions:", local_optima_positions)
plt.plot(fitness_history)
plt.xlabel("Iteration")
plt.ylabel("Best Fitness")
plt.title("Fitness Landscape")
plt.show()
