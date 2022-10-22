s=input("Enter a string: ")
if len(s)<2:
    print(s)
else:
    print(s[:2]+s[-2:])
    