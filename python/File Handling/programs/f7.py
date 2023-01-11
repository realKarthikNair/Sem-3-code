# Write a program to display all the lines in a file “python.txt” which have the word “to” in it.
# Write a program to display all the lines in a file “python.txt” which have the word “to” in it.

import os

def find_word(file, word):
    for i in file.readlines():
        if word in i:
            print(i)

find_word(open(os.path.join("files", "python.txt"), "r"), "to")