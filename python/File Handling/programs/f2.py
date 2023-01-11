# Write a Python program that takes a text file as input and returns the number of words of a given text file.
import os

def count_words(file):
    with open(file, "r") as f:
        return len(f.read().split())

print(count_words(os.path.join("files", "f1.txt")))