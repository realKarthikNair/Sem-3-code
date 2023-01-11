# Create two 2-D arrays and Plot them using matplotlib.

import numpy as np
import matplotlib.pyplot as plt

# Create two 2d NumPy arrays
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# Plot the two arrays
plt.plot(array1, array2)
plt.show()

