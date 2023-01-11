"""    8. Write a Python program to construct the following pattern, using a nested loop number.
1
22
333
4444
55555
666666
7777777
88888888
999999999
"""
def pattern8(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end="")
        print()

pattern8(9)
