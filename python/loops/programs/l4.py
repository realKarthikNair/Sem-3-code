"""    4. Write a program to print the following star pattern using the for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

def pattern4(n):
    for i in range(1, n+1):
        print("* "*i)

    for i in range(n-1, 0, -1):
        print("* "*i)


pattern4(5)