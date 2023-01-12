# Write a Python program to remove the first occurrence of a  specified element from the numpy array.

import numpy as np

def remove_first_occurrence(arr, element):
    return np.delete(arr, np.where(arr == element)[0][0])

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,5])
print(remove_first_occurrence(arr, 5))