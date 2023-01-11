# Write a Python program to read a file line by line and store it into a list.

import os

def read_file(file):
    with open(file, "r") as f:
        return f.readlines()

list_of_lines=read_file(os.path.join("files", "f1.txt"))
print(list_of_lines)