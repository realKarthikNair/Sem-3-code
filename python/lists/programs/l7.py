# Write a Python program to change the position of every n-th value with the (n+1)th in a list.

l1=[56,3,44,288,38,33]

for i in range(0,len(l1),2):
    l1[i], l1[i+1] = l1[i+1], l1[i]

print(l1)