# Write a Python program to remove spaces from dictionary keys.

def remove_spaces_from_dict_keys(d1):
    d={}
    for i, j in d1.items():
        if " " in i:
            d["".join(i.split(" "))]=j
        else:
            d[i]=j
    return d

print(remove_spaces_from_dict_keys({"name of user": "Sarah", "id":345, "dept No": 3}))      