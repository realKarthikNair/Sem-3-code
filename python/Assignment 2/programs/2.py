"""Write a python program to append data to an existing file 'python.py'. Read data to be appended from the user. Then display the contents of the entire file.
"""

data = input("Enter data to be appended to the file: ")
with open("python.py", "a") as file:
    file.write(data + "\n")
with open("python.py", "r") as file:
    print(file.read())
