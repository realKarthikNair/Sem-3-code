# Write a Python program to calculate the sum of all digits of the base to the specified power.

import math

base = int(input("Enter the base: "))
power = int(input("Enter the power: "))
sum = 0

for i in str(base**power):
    sum += int(i)

print("Sum of all digits of the base to the specified power is: ", sum)