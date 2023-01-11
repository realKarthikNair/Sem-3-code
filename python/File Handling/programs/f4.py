# Write a Python program to count the frequency of words in a file.

import os


def count_words(file):
    with open(file, "r") as f:
        data=f.read()
        return {word: data.count(word) for word in set(data.split())}

print(count_words(file=os.path.join("files", "f1.txt")))