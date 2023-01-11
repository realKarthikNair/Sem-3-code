'''Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
 If the string length is less than 2, return "Empty String".
Sample String: 'Hello Python'
Expected Result : 'Heon'
Sample String : 'Hp'
Expected Result : 'HpHp'
Sample String : 'H'
Expected Result: Empty String'''

def string_first_and_last_two_chars(s):
    return s[:2]+s[-2:] if len(s)>=2 else "Empty string"

test_cases=["Hello Python","Hp","H"]
for i in test_cases:
    print(string_first_and_last_two_chars(i))