# Write a Python program to move all zero digits to end of a given list of numbers.

l=[3,4,0,0,0,0,0,6,9]
l1=[]

for i in range(len(l)):
    if (l[i]!=0):
        continue
    else:
        l.remove(l[i])
        l.append(0)
print(l)