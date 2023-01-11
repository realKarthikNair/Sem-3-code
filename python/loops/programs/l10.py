# Write a program to accept the numbers from the user according to the range required by the user and check how many numbers are perfect numbers.

def perfect(n):
    sum = 0
    for i in range(1, n):
        if n%i == 0:
            sum += i
    return sum == n

def perfect_range(start, end):
    for i in range(start, end+1):
        if perfect(i):
            print(i)

perfect_range(1, 1000)