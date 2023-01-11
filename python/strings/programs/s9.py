'''Write a program to sort letters of word by lower to upper case format.
Sample String: ‘I am gOIng HoMe’
Expected Result: ‘amgngoe IOIHM’'''

def sort_basis_of_case(s):
    return str([i for i in s if i.islower()]+[i for i in s if not i.isupper()])

sort_basis_of_case("I am gOIng HoMe")