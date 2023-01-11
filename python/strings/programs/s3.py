"""Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'good', 'evening'
Expected Result : 'evod goening'
"""

a= input("Enter string: ")
b= input("Enter string: ")
print(b[:2]+a[2:]+" "+a[:2]+b[2:])