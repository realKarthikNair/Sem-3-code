#!/usr/bin/python

s1="Good"
s2="Morning"
s3=""

for i in range(len(s1)):
    s3+=s1[i]+s2[0-1-i]

if len(s2)>len(s1):
    s3+=s2[0:0-1-i]

print(s3)