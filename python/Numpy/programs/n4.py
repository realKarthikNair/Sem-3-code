"""Sort a 2-dimensional array by
        a. Second row
        b. Second column
"""

import numpy as np

# Create a 2-dimensional array
array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

# Sort the array by the second row
array = array[array[:, 1].argsort()]

# Sort the array by the second column
array = array[:, array[1, :].argsort()]


