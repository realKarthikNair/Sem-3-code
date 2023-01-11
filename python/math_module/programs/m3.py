"""Write a Python program to calculate the area of regular polygon.
Expected Output :
Input number of sides: 4                                                
Input the length of a side: 25                                          
The area of the polygon is:  625.0000000000001

The formula for the area of a regular polygon is given as,

A = n * s^2 / 4 * tan(pi/n)

where,
l = length of a side
n = number of sides
"""

import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = n * (s ** 2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is: ", area)
