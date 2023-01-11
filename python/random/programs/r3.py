"""Write a program to generate random String of length entered by the user. String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol except single space.
"""

import random
import string

def random_string(length):
    string0=""
    for i in range(length):
        string0+=random.choice(string.ascii_letters)
    return string0

length=int(input("Enter the length of the string: "))
print(random_string(length))
