"""Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
"""

s1="Good"
s2="Morning"

print("balaced" if set(s1).issubset(set(s2)) else "not balanced")

s1="Good"
s2="God"

print("balanced" if set(s1).issubset(set(s2)) else "not balanced")