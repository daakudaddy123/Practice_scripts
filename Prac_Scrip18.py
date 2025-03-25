# Construct a 3x3 matrix N
# a) all ones
# b) Multiply its second column by 4 and third column by 5
# c) N(1,2) = 27

import numpy as np

N = np.ones((3,3))
print(N)
print()

N[1] = N[1]*4
N[:,2] = N[:,2]*5
print(N)
print()

N[1,2] = 27
print(N)