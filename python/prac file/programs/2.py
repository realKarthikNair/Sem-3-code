"""Write a program to check if two strings are balanced. 
For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
The character’s position doesn’t matter."""

def balanced(s1, s2):
    return [True if i in s2 else False for i in s1].count(False)==0

if __name__=="__main__":
    print(balanced("abc", "cba"))
    print(balanced("abc","asb"))