### 1.     1. Write a program to print the following pattern using a loop.
###     1
###    212
###   32123
###  4321234
### 543212345
```python


def pattern(n):
    for i in range(1,n+1):
        print(" "*(n-i), end="")
        for j in range(i,0,-1):
            print(j, end="")
        for k in range(2, i+1):
            print(k, end="")
        print()

pattern(5)


```

### 2. Write a Python program to display a bar chart and
###  pie chart of the popularity of programming Languages using matplotlib.
```python

import matplotlib.pyplot as plt

def bar_chart(data):
    plt.bar(data.keys(),data.values(),color="green")
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("Popularity of programming languages")
    plt.show()

def pie_chart(data):
    plt.pie(data.values(),labels=data.keys(),autopct="%1.1f%%")
    plt.title("Popularity of programming languages")
    plt.show()

data={'Python': 22.2, 'Java': 17.6, 'PHP': 8.8, 'JavaScript': 8, 'C#': 7.7, 'C++': 6.7}
bar_chart(data)
pie_chart(data)    
```

### 3. Write a program to count the number of upper-case alphabets present in a text file “PYTHON.TXT”"""
### 
### 
### hello = open("PYTHON.TXT", "r")

### 4. Write a program to check if two strings are balanced. 
### For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
### The character’s position doesn’t matter.
```python

# Cool but not memory efficient for large strings
# def balanced(s1, s2):
#     return [False if i not in s2 else True for i in s1].count(False)==0

# again not memory efficient if strings are big
# def balanced(s1, s2):
#     return set(s1).issubset(set(s2))

def balanced(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    return True

if __name__=="__main__":
    print(balanced("abc", "cba"))
    print(balanced("abc","asb"))
```

### 5.  QN 3
### Write a Python program to replace the last element in a list with another list.
### Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
### Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
```python

def replace_last_element_with_another_list(l1, l2):
    l1[-1:]=l2
    return l1

l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]

print(replace_last_element_with_another_list(l1, l2))


```

### 6. QN 4
### Write a program to sort a tuple of tuples by 2nd item.
### Sample:
### ((‘r’,3),(‘t’,1),(‘e’,2),(‘y’,9))
### Expected Output: ((‘t’,1),(‘e’,2),(‘r’,3),(‘y’,9))
```python

def sort_tuple_of_tuples_by_second_item(t):
    s=sorted([i[1] for i in t])
    s_t=()
    for i in s:
        for j in t:
            if j[1]==i:
                s_t+=(j),
    return s_t


print(sort_tuple_of_tuples_by_second_item((('r',3),('t',1),('e',2),('y',9))))


# Different method

# def sort_tuple_of_tuples_by_second_item(t):
#     t=sorted(t, key=lambda x:x[1])
#     return t

# print(sort_tuple_of_tuples_by_second_item((('r',3),('t',1),('e',2),('y',9))))
```

### 7. Write a Python program to convert a given list of tuples to a list of lists.
### Original list of tuples: [(1, 2), (2, 3), (3, 4)]
### Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
```python

def list_of_tuples_to_list_of_lists(tuples):
    return [list(t) for t in tuples]

print(list_of_tuples_to_list_of_lists([(1, 2), (2, 3), (3, 4)]))
```

### 8.  Write a Python program to convert a binary number to decimal number using math module.
```python

import math

def binary_to_decimal(binary):
    n=len(binary)
    dec=0
    for i in binary:
        dec+=int(i)*math.pow(2,n-1)
        n-=1    
    return dec

print(binary_to_decimal("1000101"))


```

### 9. Write a program to generate 100 unique random lottery tickets
###  (each lottery number must be 10 digits long) and 
### pick two lucky tickets from it as a winner.
###  Use random module.
```python

import random

def lottery_generator(n):
    tickets=[]
    while len(tickets)!=n:
        ticket=random.randint(1000000000,9999999999)
        if ticket not in tickets:
            tickets.append(ticket)
        
    return tickets

def lucky_tickets(tickets, n):
    lucky_tickets=[]
    while len(lucky_tickets)!=n:
        lucky_ticket=random.choice(tickets)
        if lucky_ticket not in lucky_tickets:
            lucky_tickets.append(lucky_ticket)
    return lucky_tickets

tickets=lottery_generator(100)
print(f"Lucky tickets are {lucky_tickets(tickets,2)}") 

```

### 10. Write a function cubesum() that accepts an integer and returns 
### the sum of the cubes of individual digits of that number. 
### Use this function to make functions PrintArmstrong() and isArmstrong()
###  to print Armstrong numbers and to find whether is an Armstrong number.
```python

def cubesum(n):
    sum = 0
    while n>0:
        sum+=(n%10)**3
        n=n//10
    return sum

def isArmstrong(n):
    return n if n==cubesum(n) else False

def PrintArmstrong(n):
    if isArmstrong(n):
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is not an Armstrong number")

if __name__ == "__main__":
    PrintArmstrong(153)
    PrintArmstrong(154)
        
            
```

### 11. Create a 5X2 integer array from a range between 100 to 200 
### such that the difference between each element is 10. Use NumPy.
```python


import numpy as np

def array_generator(range, n, r, c):
    return np.arange(range[0],range[1],n).reshape(r, c)

print(array_generator([100,200],10,5,2))
```

