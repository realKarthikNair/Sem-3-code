"""9. Write a Python program to compute element-wise sum of given tuples.
Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6)"""

t1=(1, 2, 3, 4)
t2=(3, 5, 2, 1)
t3=(2, 2, 3, 1)

t4=tuple(map(sum,zip(t1,t2,t3)))
print(t4)

# zip(t1,t2,t3) returns a zip object, which is an iterator of tuples where
# the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.
# ie tuple(zip(t1,t2,t3))=((1, 3, 2), (2, 5, 2), (3, 2, 3), (4, 1, 1))

# map(sum,zip(t1,t2,t3)) returns an iterator of the sums of the tuples
# ie sum function runs on every tuple in the zip object
# => tuple(map(sum,zip(t1,t2,t3)))=(6, 9, 8, 6)

