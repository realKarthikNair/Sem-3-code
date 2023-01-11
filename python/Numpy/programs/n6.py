"""Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
Expected Output:
Array1: [ 0 10 20 40 60]
Array2: [0 40]
Compare each element of array1 and array2
[ True False False True False]
"""

import numpy as np

# Create two 1-D arrays
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([0, 40])

# Compare each element of array1 and array2
result = np.in1d(array1, array2)

print("Array1: ", array1)
print("Array2: ", array2)
print("Compare each element of array1 and array2")
print(result)
