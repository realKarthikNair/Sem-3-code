# Write a python program to find the area of a triangle whose sides are given.

import math


def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


print(area_of_triangle(3, 4, 5))