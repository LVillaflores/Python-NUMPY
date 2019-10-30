# Data Set
# 1. 2x + 3y = 8
#    5x + 4y = 13
# 2. 3x + 4y + 5z = 26
#    3x + 2y + z = 10
#    5x + 6y + 3z = 26
# 3. 3x + 2y + z + 4u= 26
#    5x + 3y + 2z + 7u = 10
#    6x + 2y + 3z + 4u = 26
#    5x + 2y + 4z + u = 27
# 4. 2x + 4y + 5z + 6u + 3v = 62
#    6x + 3y + 2z + u + 4v = 52
#    3x + 5y + 8z + 2u + 6v = 62
#    4x + 2y + 6z + 5u + v = 62
#    x + 4y + 3z + 6u + 2v = 49

import numpy as np

print("System of Linear Equation: AX = B")
n = int(int(input("Enter number of variables: ")))
print("Enter Matrix variables: ")
matrix1 = []
matrix2 = []

for i in range(n):
	A = []
	for j in range(n + 1):
		if j == n:
			matrix2.append(int(input("Enter Variable for B: ")))
		else:
			A.append(int(input("Enter Variables for A: ")))
	matrix1.append(A)

print(matrix1)  # A
print(matrix2)  # B

solved_matrix = np.linalg.solve(matrix1, matrix2)
print("Answer: ", solved_matrix)  # X
