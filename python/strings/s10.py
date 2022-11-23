'''Write a program in Python to count lower, upper, numeric and special characters in a string.'''

def count_chars(s):
    return {"lower":len([i for i in s if i.islower()]),"upper":len([i for i in s if i.isupper()]),"numeric":len([i for i in s if i.isnumeric()]),"special":len([i for i in s if not i.isalnum()])}

for x,y in count_chars("Karthik@cosmic42").items():
    print(f"Number of {x} characters: {y}")