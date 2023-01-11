# Write a function prodDigits() that inputs a number and returns the product of digits of that number.

def prodDigits(n):
    prod = 1
    while n>0:
        prod*=(n%10)
        n=n//10
    return prod

if __name__ == "__main__":
    print(prodDigits(1234))
    