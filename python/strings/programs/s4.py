# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'practice'
# Expected Result : 'practiceing'
# Sample String : 'eating'
# Expected Result : 'eatingly'

s=input('Enter a string: ')
if len(s)<3:
    print('Input string is too short')
    print(s)
else:
    if s[-3:]=='ing':
        print(f"{s}" 'ly')
    else:
        print(s+'ing')
