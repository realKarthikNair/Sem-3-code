'''7. Write a Python program to convert a given list of tuples to a list of lists.
Original list of tuples: [(1, 2), (2, 3), (3, 4)]'''

t=[(1, 2), (2, 3), (3, 4)]

t=[list(i) for i in t]
print(t)