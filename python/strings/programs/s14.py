# Write a program to calculate the sum and average of the digits present in a string.

def sum_avg(s):
    sum=0
    d=0
    for i in s:
        if i.isdigit():
            d+=1
            sum+=int(i)
    return sum, sum/d

print(sum_avg("abc123"))
