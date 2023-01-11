# Write a Python program to capitalize first and last letters of each word of a given string.

def capitalize(s):
    return ' '.join([w[0].upper() + w[1:-1] + w[-1].upper() for w in s.split()])

print(capitalize('Here is a school'))