'''Write a program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''


def gen_x_pow_dict(x):
    return {i: i**2 for i in range (1, x+1)}

print(gen_x_pow_dict(5))