"""Write a function cubesum() that accepts an integer and returns the sum of the cubes of individual digits of that number. Use this function to make functions PrintArmstrong() and isArmstrong() to print Armstrong numbers and to find whether is an Armstrong number.
"""

def cubesum(n):
    sum = 0
    while n>0:
        sum+=(n%10)**3
        n=n//10
    return sum

def isArmstrong(n):
    return n if n==cubesum(n) else False

def PrintArmstrong(n):
    if isArmstrong(n):
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is not an Armstrong number")

if __name__ == "__main__":
    PrintArmstrong(153)
    PrintArmstrong(154)
        
            
