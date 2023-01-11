# Write a Python program to find the roots of a quadratic equation.

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