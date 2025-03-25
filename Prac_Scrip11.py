# Change temp from c to f using numpy

import numpy as np

c = [5,11.1,23,9]
c1 = np.array(c)
F = ((9*c1)/5) +32
print(F)

# Values of Sin Cos Tan by Numpy

ang = int(input("Write the angle =",))
ang_radians = ang*(np.pi/180)
print(np.sin(ang))
print(np.sin(ang))
print(np.tan(ang))