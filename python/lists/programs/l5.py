# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.

l=['a','b']
n=int(input("Enter a number: "))
l1=[]
for i in range(1,n+1):
    for j in l :
        l1.append(j+str(i))
print(l1)
