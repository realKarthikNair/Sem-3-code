"""Write a Python program to convert string values of a given dictionary, into integer/float datatypes.
Sample:
Original list:
[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
String values of a given dictionary, into integer types:
[{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
"""

def convert_dict(dict1):
    return [{k: int(v) for k, v in d.items()} for d in dict1]

print(convert_dict([{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]))
