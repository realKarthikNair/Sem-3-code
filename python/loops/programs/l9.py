# Write a program to accept an integer number from the user and display its binary equivalent.

def binary(n):
    return bin(n)[2:]

print(binary(69))

# num=int(input("Enter an integer: "))
# bin=""

# while (num!=0):
#     bin=bin+str(num%2)
#     num=num//2

# print(bin[::-1])