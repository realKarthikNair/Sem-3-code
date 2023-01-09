''' QN 4 DIFFERENT METHOD
Write a program to sort a tuple of tuples by 2nd item.
Sample:
((‘r’,3),(‘t’,1),(‘e’,2),(‘y’,9))
Expected Output: ((‘t’,1),(‘e’,2),(‘r’,3),(‘y’,9))'''

def sort_tuple_of_tuples_by_second_item(t):
    t=sorted(t, key=lambda x:x[1])
    return t

print(sort_tuple_of_tuples_by_second_item((('r',3),('t',1),('e',2),('y',9))))