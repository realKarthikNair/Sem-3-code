# Write a program to count the number of upper-case alphabets present in a text file “PYTHON.TXT”.

import os

def count_uppercase(file):
    with open(file, "r") as f:
        return sum(1 for char in f.read() if char.isupper())

print(count_uppercase(os.path.join("files", "f1.txt")))