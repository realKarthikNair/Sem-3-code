# Write a Python program to convert a binary number to decimal number.

import math

def binary_to_decimal(binary):
    n=len(binary)
    dec=0
    for i in binary:
        dec+=int(i)*math.pow(2,n-1)
        n-=1    
    return dec

print(binary_to_decimal("1000101"))