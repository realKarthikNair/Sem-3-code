"""Write a function sumPdivisors() that finds the sum of proper divisors of a number. 
Proper divisors of a number are those numbers by which the number is divisible, except the number itself. 
For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18.
"""

def sumPdivisors(n):
    sum = 0
    for i in range(1,n):
        if n%i==0:
            print(i)
            sum+=i
    return sum

if __name__ == "__main__":
    print(sumPdivisors(36))