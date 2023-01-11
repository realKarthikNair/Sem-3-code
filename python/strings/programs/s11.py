"""Write a program to create a string made of the first, middle and last character. If the number of characters in the string is even, consider first letter out of the two middle characters as middle one.
Sample String: ‘Plane’
Expected Result: ‘Pae’
Sample String: ‘Planer’
Expected Result: ‘Par
"""

def get_middle_char(s):
    if len(s)%2==0:
        return s[0]+s[len(s)//2-1]+s[-1]
    else:
        return s[0]+s[len(s)//2]+s[-1]

print(get_middle_char("Plane"))
print(get_middle_char("Planer"))

