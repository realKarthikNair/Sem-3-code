# Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.

import numpy as np
x = np.arange(10, 34, 1)
x = x.reshape(8, 3)
print(x)
print(np.split(x, 4))

