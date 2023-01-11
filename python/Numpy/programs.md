Karthik Nair | 3EA | 00229802021

# Numpy Programs

### 1.  Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10.
```python

import numpy as np
x = np.arange(100, 200, 10)
x = x.reshape(5, 2)
print(x)

```

### 2.  Write a Python program to create a pie chart of the popularity of programming Languages using matplotli
```python

import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.pie(popularity, labels = languages, autopct = '%1.1f%%')
plt.axis('equal')
plt.title('Popularity of Programming Languages')
plt.show()

```

### 3.  Create a result array by adding the two NumPy arrays. Next, modify the result array by calculating the square of each element.
```python

import numpy as np

# Create two NumPy arrays
array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

# Add the two arrays and create a result array
result_array = array1 + array2

# Modify the result array by calculating the square of each element
result_array = result_array ** 2

print(result_array)


```

### 4.  Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
```python

import numpy as np
x = np.arange(10, 34, 1)
x = x.reshape(8, 3)
print(x)
print(np.split(x, 4))


```

### 5. Sort a 2-dimensional array by
###         a. Second row
###         b. Second column
### 
```python

import numpy as np

# Create a 2-dimensional array
array = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

# Sort the array by the second row
array = array[array[:, 1].argsort()]

# Sort the array by the second column
array = array[:, array[1, :].argsort()]



```

### 6.  Create two 2-D arrays and Plot them using matplotlib.
```python

import numpy as np
import matplotlib.pyplot as plt

# Create two 2d NumPy arrays
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# Plot the two arrays
plt.plot(array1, array2)
plt.show()


```

### 7. Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
### Expected Output:
### Array1: [ 0 10 20 40 60]
### Array2: [0 40]
### Compare each element of array1 and array2
### [ True False False True False]
### 
```python

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

```

### 8.  Write a NumPy program to find common values between two arrays.
```python

import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])

common_values = np.intersect1d(array1, array2)
print(common_values)


```

### 9.  Write a NumPy program to find the union of two arrays.
```python

import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])

union_values = np.union1d(array1, array2)
print(union_values)

```

### 10.   Write a Python program to display a bar chart of the popularity of programming Languages using matplotlib.
```python

import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(languages, popularity)
plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Languages')
plt.show()


```

