"""6. Write a Python program to split a given dictionary of lists into list of dictionaries. 
Sample:
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""

def split_dict(dict1):
    return [dict(zip(dict1, i)) for i in zip(*dict1.values())]


print(split_dict({'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}))