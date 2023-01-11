"""Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '#', except the first char itself.
Sample String : 'extent'
Expected Result : 'ext#nt'
"""

s=input("Enter a string: ")
print(s[0]+s[1:].replace(s[0],'#'))