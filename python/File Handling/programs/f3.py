# Write a Python program to assess if a file is closed or not.

import os

def is_closed(file):
    return file.closed


print(is_closed(open(os.path.join("files", "f1.txt"), "r")))    