### 1. Write a  python program to create a  plotting of years of compounding v/s value of principal using the pyplot library. Assume reasonable values for principal, interest rate, and years.
### 
```python

import matplotlib.pyplot as plt

def plot_compounding(principal, interest_rate, years):
    x = list(range(years + 1))
    y = [principal * (1 + interest_rate) ** i for i in x]
    plt.plot(x, y)
    plt.xlabel('Years')
    plt.ylabel('Value of Principal')
    plt.title('Value of Principal over Time')
    plt.show()
    
plot_compounding(1000, 0.05, 10)

```

### 2. Write a python program to append data to an existing file 'python.py'. Read data to be appended from the user. Then display the contents of the entire file.
### 
```python

data = input("Enter data to be appended to the file: ")
with open("python.py", "a") as file:
    file.write(data + "\n")
with open("python.py", "r") as file:
    print(file.read())

```

### 3. Write a Python program to read a text file and do following:
###         a. Print no. of words
###         b. Print no. Statements
### 
```python

with open("file.txt", "r") as file:
    data = file.read()
    print("No. of words:", len(data.split()))
    print("No. of statements:", len(data.split("."))-1)


```

### 4.  Write a Python program to remove the first occurrence of a  specified element from the numpy array.
```python

import numpy as np

def remove_first_occurrence(arr, element):
    return np.delete(arr, np.where(arr == element)[0][0])

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,5])
print(remove_first_occurrence(arr, 5))
```

