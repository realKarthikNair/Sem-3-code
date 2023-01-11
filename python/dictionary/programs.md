Karthik Nair | 3EA | 00229802021

# Dictionary Programs

### 1.  Write a program to sort (ascending and descending) a dictionary by value.
```python

# def sort_dict(d):
#     return sorted(d.items(), key=lambda x: x[1])

def keys(di):
    return di[1]

def sort_dict(d):
    return sorted(list(d.items()), key=keys)

print(sort_dict({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}))
```

### 2. Write a program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
### Sample Dictionary ( n = 5) :
### Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```python


def gen_x_pow_dict(x):
    return {i: i**2 for i in range (1, x+1)}

print(gen_x_pow_dict(5))
```

### 3. Write a Python program to combine two dictionaries adding values for common keys.
### Sample Dictionaries:
### d1 = {'a': 100, 'b': 200, 'c':300}
### d2 = {'a': 300, 'b': 200, 'd':400}
### Sample output: Counter({'a': 400, 'b': 400, 'c': 300, 'd': 400})
```python

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
```

### 4.  Write a Python program to remove spaces from dictionary keys.
```python

def remove_spaces_from_dict_keys(d1):
    d={}
    for i, j in d1.items():
        if " " in i:
            d["".join(i.split(" "))]=j
        else:
            d[i]=j
    return d

print(remove_spaces_from_dict_keys({"name of user": "Sarah", "id":345, "dept No": 3}))      
```

### 5.  Write a Python program to replace dictionary values with their average.
```python


def replace_with_avg(d):
    avg=sum(d.values())/len(d.values())
    for i in d:
        d[i]=avg
    return d


print(replace_with_avg({2:2, 32:1}))
```

### 6. 6. Write a Python program to split a given dictionary of lists into list of dictionaries. 
### Sample:
### Original dictionary of lists:
### {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
### Split said dictionary of lists into list of dictionaries:
### [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
### 
```python

def split_dict(dict1):
    return [dict(zip(dict1, i)) for i in zip(*dict1.values())]


print(split_dict({'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}))
```

### 7. Write a Python program to convert string values of a given dictionary, into integer/float datatypes.
### Sample:
### Original list:
### [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
### String values of a given dictionary, into integer types:
### [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
### 
```python

def convert_dict(dict1):
    return [{k: int(v) for k, v in d.items()} for d in dict1]

print(convert_dict([{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]))

```

