# Write a Python program to move spaces to the front of a given string.

def move_spaces(s):
    return s.count(" ")*" " +"".join(s.split())

print(move_spaces('Here is a school'))
