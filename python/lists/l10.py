l=[3,4,0,0,0,0,0,6,9]
l1=[]

# c=l.count(0)

# for i in l:
#     if i!=0: l1.append(i)

# for i in range(c): l1.append(0)
# print(l1)

#    if 
    # if i!=0:
    #     l1.append(i)
    # else:
for i in range(len(l)):
    if (l[i]!=0):
        continue
    else:
        l.remove(l[i])
        l.append(0)
print(l)