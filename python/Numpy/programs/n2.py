# Create a result array by adding the two NumPy arrays. Next, modify the result array by calculating the square of each element.

import numpy as np

# Create two NumPy arrays
array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

# Add the two arrays and create a result array
result_array = array1 + array2

# Modify the result array by calculating the square of each element
result_array = result_array ** 2

print(result_array)

