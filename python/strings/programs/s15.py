# Write a program to reverse a string if it's length is a multiple of 4.

def reverse(s, n):
    if len(s) % n != 0:
        return
    return s[::-1]

print(reverse('abcd', 4))