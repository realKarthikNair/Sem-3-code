Karthik Nair | 3EA | 00229802021

# Loops

### 1. Write a program to print the following number pattern using a loop.
### 1 
### 1 2 
### 1 2 3 
### 1 2 3 4 
### 1 2 3 4 5
### 
```python

def pattern1(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

pattern1(5)
```

### 2.  Write a program to accept the numbers from the user according to the range required by the user and check how many numbers are perfect numbers.
```python

def perfect(n):
    sum = 0
    for i in range(1, n):
        if n%i == 0:
            sum += i
    return sum == n

def perfect_range(start, end):
    for i in range(start, end+1):
        if perfect(i):
            print(i)

perfect_range(1, 1000)
```

### 3. Write a program to use for loop to print the following reverse number pattern.
### 5 4 3 2 1 
### 4 3 2 1 
### 3 2 1 
### 2 1 
### 1
### 
```python

def pattern2(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

pattern2(5)
```

### 4.  Write a program to reverse a given integer number.
```python

def reverse_number(n):
    return (int(str(n)[::-1]))

print(reverse_number(12345))
```

### 5.     4. Write a program to print the following star pattern using the for loop.
### * 
### * * 
### * * * 
### * * * * 
### * * * * * 
### * * * * 
### * * * 
### * * 
### *
### 
```python

def pattern4(n):
    for i in range(1, n+1):
        print("* "*i)

    for i in range(n-1, 0, -1):
        print("* "*i)


pattern4(5)
```

### 6. Write a Python program to check the validity of password input by users. If invalid password, ask the user to enter it again.
### Validation :
### At least 1 letter between [a-z] and 1 letter between [A-Z].
### At least 1 number between [0-9].
### At least 1 character from [$#@].
### Minimum length 6 characters.
### Maximum length 16 characters.
### 
```python

import re

def check_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

def main():
    password = input("Enter password: ")
    while not check_password(password):
        print("Invalid password")
        password = input("Enter password: ")
    print("Valid password")

main()

```

### 7.  Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.
```python

for i in range(100, 401):
    # find if each digit is an even number
    for j in str(i):
        if int(j)%2 != 0:
            break
    else:
        print(i)

```

### 8.  7. Write a Python program to print alphabet pattern 'A'.
```python
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *****                                                                 
#  *   *                                                                  
#  *   *                                                                  
#  *   *

for i in range(7):
    if (i==0 or i==3):
        if (i==0):
            print(" "+"*"*3)
        elif (i==3):
            print("*"*5)
    else:
        print("*"+(" "*3)+"*")
        
```

### 9.     8. Write a Python program to construct the following pattern, using a nested loop number.
### 1
### 22
### 333
### 4444
### 55555
### 666666
### 7777777
### 88888888
### 999999999
### 
```python
def pattern8(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end="")
        print()

pattern8(9)

```

### 10.  Write a program to accept an integer number from the user and display its binary equivalent.
```python

def binary(n):
    return bin(n)[2:]

print(binary(69))

# num=int(input("Enter an integer: "))
# bin=""

# while (num!=0):
#     bin=bin+str(num%2)
#     num=num//2

# print(bin[::-1])
```

