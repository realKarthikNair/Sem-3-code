Karthik Nair | 3EA | 00229802021

# Math Module Programs

### 1.  Write a Python program to calculate surface volume and area of a sphere.
```python

import math

radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * math.pi * radius**3
area = 4 * math.pi * radius**2

print("Volume of the sphere is: ", volume)
print("Area of the sphere is: ", area)

```

### 2.  Write a Python program to calculate the sum of all digits of the base to the specified power.
```python

import math

base = int(input("Enter the base: "))
power = int(input("Enter the power: "))
sum = 0

for i in str(base**power):
    sum += int(i)

print("Sum of all digits of the base to the specified power is: ", sum)
```

### 3. Write a Python program to calculate the area of regular polygon.
### Expected Output :
### Input number of sides: 4                                                
### Input the length of a side: 25                                          
### The area of the polygon is:  625.0000000000001
### 
### The formula for the area of a regular polygon is given as,
### 
### A = n * s^2 / 4 * tan(pi/n)
### 
### where,
### l = length of a side
### n = number of sides
### 
```python

import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = n * (s ** 2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is: ", area)

```

### 4.  Write a Python program to convert a binary number to decimal number.
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

### 5.  Write a code to solve the equation z = |x − y| * (x + y).
```python

import math

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = abs(x - y) * (x + y)
print("The value of z is: ", z)


```

### 6.  Write a python program to find the area of a triangle whose sides are given.
```python

import math


def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


print(area_of_triangle(3, 4, 5))
```

### 7.  Write a Python program to find the roots of a quadratic equation.
```python

import math

def quadratic_equation(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return root1, root2
    elif d == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"

print(quadratic_equation(1, 2, 3))
print(quadratic_equation(1, 2, -3))
```

