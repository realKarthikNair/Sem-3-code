# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

l=[i**2  for i in range(1,31)]
l=l[:5]+l[-5:]
print(l)

