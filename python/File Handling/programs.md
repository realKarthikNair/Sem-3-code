Karthik Nair | 3EA | 00229802021

# File Handling

### 1.  Write a Python program to combine each line from first file with the corresponding line in second file.
```python

import os

def combine_files(file1, file2):
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            for line1, line2 in zip(f1, f2):
                print(line1+line2)

combine_files(os.path.join("files", "f1.txt"), os.path.join("files", "f2.txt"))
```

### 2.  Write a Python program that takes a text file as input and returns the number of words of a given text file.
```python
import os

def count_words(file):
    with open(file, "r") as f:
        return len(f.read().split())

print(count_words(os.path.join("files", "f1.txt")))
```

### 3.  Write a Python program to assess if a file is closed or not.
```python

import os

def is_closed(file):
    return file.closed


print(is_closed(open(os.path.join("files", "f1.txt"), "r")))    
```

### 4.  Write a Python program to count the frequency of words in a file.
```python

import os


def count_words(file):
    with open(file, "r") as f:
        data=f.read()
        return {word: data.count(word) for word in set(data.split())}

print(count_words(file=os.path.join("files", "f1.txt")))
```

### 5.  Write a Python program to read a file line by line and store it into a list.
```python

import os

def read_file(file):
    with open(file, "r") as f:
        return f.readlines()

list_of_lines=read_file(os.path.join("files", "f1.txt"))
print(list_of_lines)
```

### 6.  Write a program to count the number of upper-case alphabets present in a text file “PYTHON.TXT”.
```python

import os

def count_uppercase(file):
    with open(file, "r") as f:
        return sum(1 for char in f.read() if char.isupper())

print(count_uppercase(os.path.join("files", "f1.txt")))
```

### 7.  Write a program to display all the lines in a file “python.txt” which have the word “to” in it.
```python
# Write a program to display all the lines in a file “python.txt” which have the word “to” in it.

import os

def find_word(file, word):
    for i in file.readlines():
        if word in i:
            print(i)

find_word(open(os.path.join("files", "python.txt"), "r"), "to")
```

