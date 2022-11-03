s=input("Enter a string: ")
vc=0
cc=0
for i in s:
    if i in ['a','e','i','o','u']:
        vc+=1
    else:
        cc+=1
print("No of vowels: ",vc)
print("No of consonants: ",cc)
