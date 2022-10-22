num=int(input("Enter an integer: "))
bin=""

while (num!=0):
    bin=bin+str(num%2)
    num=num//2

print(bin[::-1])