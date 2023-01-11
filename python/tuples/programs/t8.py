"""Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
Original list of tuples:
[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[9, -1, 7, 8]"""


t=[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
t=[sum(i) for i in t]
print(t)