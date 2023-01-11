# Write a code to solve the equation z = |x − y| * (x + y).

import math

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = abs(x - y) * (x + y)
print("The value of z is: ", z)

