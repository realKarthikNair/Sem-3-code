# Write a Python program to combine each line from first file with the corresponding line in second file.

import os

def combine_files(file1, file2):
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            for line1, line2 in zip(f1, f2):
                print(line1+line2)

combine_files(os.path.join("files", "f1.txt"), os.path.join("files", "f2.txt"))