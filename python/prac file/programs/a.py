"""Write a program to print the following pattern using a loop.
    1
   212
  32123
 4321234
543212345"""


def pattern(n):
    for i in range(1,n+1):
        print(" "*(n-i), end="")
        for j in range(i,0,-1):
            print(j, end="")
        for k in range(2, i+1):
            print(k, end="")
        print()

pattern(5)

