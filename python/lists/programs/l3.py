# Write a Python program to print the numbers of a specified list after removing even numbers from it.

l=[23,45,22,53,24,10,55,8]
l1=[]
for i in l:
    if (i%2!=0):
        l1.append(i)

print(l1)

