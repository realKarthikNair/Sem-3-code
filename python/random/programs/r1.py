# Write a program to generate 3 random integers between 100 and 999 which are divisible by 5.

import random

for i in range(3):
    print(random.randrange(100, 999, 5))
