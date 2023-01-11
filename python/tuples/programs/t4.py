# Write a program to copy specific elements from one tuple to a new tuple.

def copy_els(indexes, t):
    new=()
    for i in indexes:
        new+=(t[i],)
    return new

a=eval(input("Enter a tuple: "))
i=eval(input("Enter indexes you want to copy: "))

print(copy_els(i, a))