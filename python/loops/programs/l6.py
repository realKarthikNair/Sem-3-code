# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.

for i in range(100, 401):
    # find if each digit is an even number
    for j in str(i):
        if int(j)%2 != 0:
            break
    else:
        print(i)
