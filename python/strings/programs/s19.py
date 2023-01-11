# Write a Python program to replace each character of a word of length five and more with hash character (#).

data='''What's the difference between a dead dog in the road and a dead
	lawyer in the road?
A:	There are skid marks in front of the dog.'''

# l=data.split()
# for i in  l:
#     if len(i)>=5:
#       print(  i.replace(i, "#"*len(i)), end=" ")
#     else:
#         print(i, end=" ")

print(" ".join([i.replace(i, "#"*len(i)) if len(i)>=5 else i for i in data.split() ]))

# data=" ".join([i.replace(i, "#"*len(i)) for i in data.split()  if len(i)>5  ])
# print(data)
