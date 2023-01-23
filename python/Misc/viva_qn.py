a="Karthik8888India"

b=c=d=""

for i in range(len(a)):
    if not a[i].isdigit():
        b+=a[i]
    else:
        break

for j in range(i, len(a)):
    if a[j].isdigit():
        c+=a[j]
    else:
        break
        
for k in range(j, len(a)):
    if not a[k].isdigit():
        d+=a[k]
    else:
        break

print(b,c,d,sep="\n")