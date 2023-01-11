'''Write a Python program to convert a given tuple of positive integers into an integer.
Original tuple:
(10, 20, 40, 5, 70)
Convert the said tuple of positive integers into an integer:
102040570'''

def get_number_from_tuple(t):
    try:
        return int("".join(map(str,t)))
    except (TypeError, ValueError):
        return 0

print(get_number_from_tuple((10, 20, 40, 5, 70)))