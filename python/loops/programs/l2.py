"""Write a program to use for loop to print the following reverse number pattern.
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""

def pattern2(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

pattern2(5)