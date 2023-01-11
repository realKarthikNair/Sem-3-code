# Write a NumPy program to find common values between two arrays.

import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])

common_values = np.intersect1d(array1, array2)
print(common_values)

