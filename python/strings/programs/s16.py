"""Write a Python program to reverse words in a string.
Sample String: ‘Here is a school’
Expected Result: ‘school a is Here’
"""

def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(reverse_words('Here is a school'))