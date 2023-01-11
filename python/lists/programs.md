Karthik Nair | 3EA | 00229802021

# List Programs

### 1.  Write a program to remove duplicates from a list.
```python

l=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    l.append(int(input()))
print(l)
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print("list without duplicates: ",l1)
```

### 2.  Write a Python program to move all zero digits to end of a given list of numbers.
```python

l=[3,4,0,0,0,0,0,6,9]
l1=[]

for i in range(len(l)):
    if (l[i]!=0):
        continue
    else:
        l.remove(l[i])
        l.append(0)
print(l)
```

### 3.  Write a Python function that takes two lists and returns True if they have at least one common member.
```python

def common(l1,l2):
    for i in l1:
        if i in l2:
            print("Common element found!")
            break
l1=[23,45,2,44,33]
l2=[7,67,88,66, 44]
common(l1,l2)
    #[print("Common elements!") if i in l2 for i in l1]
```

### 4.  Write a Python program to print the numbers of a specified list after removing even numbers from it.
```python

l=[23,45,22,53,24,10,55,8]
l1=[]
for i in l:
    if (i%2!=0):
        l1.append(i)

print(l1)


```

### 5.  Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
```python

l=[i**2  for i in range(1,31)]
l=l[:5]+l[-5:]
print(l)


```

### 6.  Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
```python

l=['a','b']
n=int(input("Enter a number: "))
l1=[]
for i in range(1,n+1):
    for j in l :
        l1.append(j+str(i))
print(l1)

```

### 7.  Write a Python program to find common items from two lists.
```python

l1=[10,12,4,56,38]
l2=[56,3,44,288,38]
for i in l1:
    if i in l2:
        print(i)

```

### 8.  Write a Python program to change the position of every n-th value with the (n+1)th in a list.
```python

l1=[56,3,44,288,38,33]

for i in range(0,len(l1),2):
    l1[i], l1[i+1] = l1[i+1], l1[i]

print(l1)
```

### 9.  Write a Python program to convert a list of multiple integers into a single integer.
```python

l=[13,33,60]
s=""
for i in l:
    s+=str(i)
print(int(s))


```

### 10.  Write a Python program to replace the last element in a list with another list.
```python

l=[10,20,20,40,50]
l1=[1,2,3,4]
l.pop(-1)
l.extend(l1)
print(l)
```

