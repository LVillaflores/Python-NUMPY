import numpy as np

a = np.zeros((2, 3))
b = np.arange(15).reshape(3, 5)
c = np.ones((2, 2, 2))
d = np.random.random((2, 3))

# Operation
e = np.array([[2, 3], [5, 4]])
f = np.array([[8], [13]])
g = np.linalg.inv(e)
h = g @ f

print(a)
print(b)
print(c)
print(d)
print(e)
print(h)
