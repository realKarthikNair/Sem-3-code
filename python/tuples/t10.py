'''Write a Python program to check if a specified element presents in a tuple of tuples.
Original list:
(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
Check if White presenet in said tuple of tuples!
True
Check if White presenet in said tuple of tuples!
True
Check if Olive presenet in said tuple of tuples!
False'''


def check_for_specific_element(t, element):
    for i in t:
        if element in i:
            return True

tuple0=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

elements=("Olive", "White")

for i in elements:
    print(f"{i} ",end="")
    if not check_for_specific_element(tuple0, i):
        print("not ", end="")
    print("present")

        
