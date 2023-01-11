"""Write a Python program to check the validity of password input by users. If invalid password, ask the user to enter it again.
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""

import re

def check_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

def main():
    password = input("Enter password: ")
    while not check_password(password):
        print("Invalid password")
        password = input("Enter password: ")
    print("Valid password")

main()
