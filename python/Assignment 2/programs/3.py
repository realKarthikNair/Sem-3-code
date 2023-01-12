"""Write a Python program to read a text file and do following:
        a. Print no. of words
        b. Print no. Statements
"""

with open("file.txt", "r") as file:
    data = file.read()
    print("No. of words:", len(data.split()))
    print("No. of statements:", len(data.split("."))-1)

