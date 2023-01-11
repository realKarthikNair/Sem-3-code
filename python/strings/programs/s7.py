# Write a program to count the occurrence of each character in a word.

def count_char_occurence(s):
    return {i:s.count(i) for i in s}

for x,y in count_char_occurence("Hogwarts is Home").items():
    print(f"{x} Appears {y} times")
