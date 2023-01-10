"""Write a program to know the cursor position and print the text according to specifications 
given below: 
● Print the initial position 
● Move the cursor to 4th position 
● Display next 5 characters 
● Move the cursor to the next 10 characters 
● Print the current cursor position 
● Print next 10 characters from the current cursor position"""

import os

file=open(os.path.join("files","demo.txt"),"rb")

print(f"Initial position: {file.tell()}")

file.seek(4)
print(f"Next 5 chars from 4th position: {file.read(5)}")

file.seek(10,1)
print(f"Current cursor position: {file.tell()}")

print(f"Next 10 chars from current cursor position: {file.read(10)}")