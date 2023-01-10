"""Write a program to count the number of upper-case alphabets present in a text file “PYTHON.TXT”
"""
import os

def countUpperCase(file):
    count = 0
    for line in file:
        for char in line:
            if char.isupper():
                count += 1
    return count

file = open(os.path.join("files", "PYTHON.TXT"), "r")

print(countUpperCase(file))