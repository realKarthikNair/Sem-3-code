"""Write a Python program to combine two dictionaries adding values for common keys.
Sample Dictionaries:
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'c': 300, 'd': 400})"""

def combine_values(d1, d2):
    d3={**d1, **d2}
    d4={}
    for i,j in d3.items():
        if i in d1.keys() and i in d2.keys():
            d4[i]=d1[i]+d2[i]
        else:
            d4[i]=j
    return d4


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print(combine_values(d1, d2))



# def combine_values(d1, d2):  
#     d3={}
#     for i in set(d1.keys).intersection(set(d2.keys)):
#         d3[i]=d1[i]+d2[i]
#     for i in set(d1.keys)-set(d2.keys):
#         d3[i]=d1[i]
#     for i in set(d2.keys)-set(d1.keys):
#         d3[i]=d2[i]
#     return d3


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# print(combine_values(d1, d2))