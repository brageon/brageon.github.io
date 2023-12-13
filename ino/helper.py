'''
Wrangling helper to transition between combine.py and frequency.py
'''
with open('w1.txt', 'r') as f:
    data = f.read()
data = data.replace('\n', ', ')
with open('w1.txt', 'w') as f:
    f.write(data)
'''
Use this after brute.py to recalibrate for better unit testing.

import numpy as np
C = np.array([6, 4, 4, 6, 6, 7, 5, 4, 6, 6])
Co = np.array([7, 5, 6, 6, 5, 4, 4, 4, 4, 5])
mse = np.mean((C - Co)**2)
error_rate = np.sum(C != Co) / len(C)
print("Mean squared error:", mse)
print("Error rate:", error_rate)
'''
