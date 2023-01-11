# Write a program to sort (ascending and descending) a dictionary by value.

# def sort_dict(d):
#     return sorted(d.items(), key=lambda x: x[1])

def keys(di):
    return di[1]

def sort_dict(d):
    return sorted(list(d.items()), key=keys)

print(sort_dict({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}))