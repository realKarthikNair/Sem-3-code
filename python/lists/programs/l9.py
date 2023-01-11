# Write a Python program to replace the last element in a list with another list.

l=[10,20,20,40,50]
l1=[1,2,3,4]
l.pop(-1)
l.extend(l1)
print(l)