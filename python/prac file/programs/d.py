'''Write a program to sort a tuple of tuples by 2nd item.
Sample:
((‘r’,3),(‘t’,1),(‘e’,2),(‘y’,9))
Expected Output: ((‘t’,1),(‘e’,2),(‘r’,3),(‘y’,9))'''

def sort_tuple_of_tuples_by_second_item(t):
    s=sorted([i[1] for i in t])
    s_t=()
    for i in s:
        for j in t:
            if j[1]==i:
                s_t+=(j),
    return s_t


print(sort_tuple_of_tuples_by_second_item((('r',3),('t',1),('e',2),('y',9))))


# Different method

# def sort_tuple_of_tuples_by_second_item(t):
#     t=sorted(t, key=lambda x:x[1])
#     return t

# print(sort_tuple_of_tuples_by_second_item((('r',3),('t',1),('e',2),('y',9))))