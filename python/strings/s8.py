'''Write a program to convert lower letter to upper and upper letter to lower in a string.
Sample String: ‘Hello Python’
Expected Result: ‘hELLO pYTHON’'''

def convert_case(s):
    return s.swapcase()

print(convert_case("Hello Python"))