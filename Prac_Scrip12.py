# Two Dimentional array

import numpy as np

m = np.array([[1,2,3],[4,7,11]]) 
print(m)
n = np.arange(1,7).reshape(2,3)
print(n)
x = np.ones([3,3])
print(x)
y = np.zeros((2,3))
print(y)

# Extracting the elements from a matrix

print(m[1][2])
print(m[1])
print(m[:,2])