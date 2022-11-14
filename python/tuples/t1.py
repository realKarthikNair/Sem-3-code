# Write a program to remove duplicates from a tuple.

def remove_duplicates(t):
    return tuple(set(t))

def remove_duplicates_2(t):
    new=()
    for i in t:
        if i not in new:
            new+=(i,)
    return new


print(remove_duplicates(eval(input("Enter a tuple: "))))
print(remove_duplicates_2(eval(input("Enter a tuple: "))))