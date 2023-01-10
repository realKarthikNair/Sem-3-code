"""Create a dictionary whose keys are month names and whose values are the number of days 
in the corresponding months. 
        a. Ask the user to enter a month name and use the dictionary to tell them how many 
              days are in the month.
        b. Print out all keys in the alphabetical order
        c. Print out all the months with 31 days
        d. Print out the key value pairs sorted by number of days in each month
        """

months={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}

# a
month=input("Enter a month name: ")
print(months[month])

# b
print(sorted(months.keys()))

# c 
print([i for i in months if months[i]==31])

# d
print(sorted(months.items(), key=lambda x:x[1]))