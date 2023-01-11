"""Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
Sample String: ‘Good’, ‘Morning’
Expected Result: ‘GgonoidnMor’
"""

s1="Good"
s2="Morning"
s3=""

e=-1
for i in range(len(s1)):
    s3+=s1[i]+s2[e]
    e-=1

if len(s2)>len(s1):
    s3+=s2[0:e+1]

print(s3)