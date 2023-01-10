"""Write a Python program to convert a given list of tuples to a list of lists.
Original list of tuples: [(1, 2), (2, 3), (3, 4)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]"""

def list_of_tuples_to_list_of_lists(tuples):
    return [list(t) for t in tuples]

print(list_of_tuples_to_list_of_lists([(1, 2), (2, 3), (3, 4)]))