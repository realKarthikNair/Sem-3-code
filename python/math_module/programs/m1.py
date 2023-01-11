# Write a Python program to calculate surface volume and area of a sphere.

import math

radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * math.pi * radius**3
area = 4 * math.pi * radius**2

print("Volume of the sphere is: ", volume)
print("Area of the sphere is: ", area)
