"""Create a 5X2 integer array from a range between 100 to 200 
such that the difference between each element is 10. Use NumPy."""


import numpy as np

def array_generator(range, n, r, c):
    return np.arange(range[0],range[1],n).reshape(r, c)

print(array_generator([100,200],10,5,2))