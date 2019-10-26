import numpy as np

A = np.array([[2, 3],
              [5, 4]])
B = np.array([[8],
              [13]])
C = np.linalg.inv(A)
D = C @ B

print(D)