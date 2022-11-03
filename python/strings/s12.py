#!/usr/bin/python

s1="Good"
s2="Morning"
s3=""

e=-1
for i in range(len(s1)):
    s3+=s1[i]+s2[e]
    e-=1

if len(s2)>len(s1):
    s3+=s2[0:len(s2)-len(s1)]
    
print(s3)