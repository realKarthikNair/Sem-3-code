"""Write a program to check if two strings are balanced. 
For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
The character’s position doesn’t matter."""

# Cool but not memory efficient for large strings
# def balanced(s1, s2):
#     return [False if i not in s2 else True for i in s1].count(False)==0

# again not memory efficient if strings are big
# def balanced(s1, s2):
#     return set(s1).issubset(set(s2))

def balanced(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    return True

if __name__=="__main__":
    print(balanced("abc", "cba"))
    print(balanced("abc","asb"))