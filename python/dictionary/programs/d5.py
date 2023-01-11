# Write a Python program to replace dictionary values with their average.


def replace_with_avg(d):
    avg=sum(d.values())/len(d.values())
    for i in d:
        d[i]=avg
    return d


print(replace_with_avg({2:2, 32:1}))