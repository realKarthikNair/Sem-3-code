'''Write a Python program to convert a tuple of string values to a tuple of integer values.
Original tuple values:
(('333', '33'), ('1416', '55'))
New tuple values:
((333, 33), (1416, 55))'''

def convert_string_values_to_int(t):
    i_t=()
    for i in t:
        i_t+=tuple(map(int,i)),
    return i_t

print(convert_string_values_to_int((('333', '33'), ('1416', '55'))))

