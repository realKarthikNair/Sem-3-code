l=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    l.append(int(input()))
print(l)
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print("list without duplicates: ",l1)