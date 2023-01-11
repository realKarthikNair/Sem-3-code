"""Write a program to Create a CSV file by entering user-id and password, read and search 
the password for given user id.
"""


import csv

# create a new CSV file with a user-id and password
def create_csv(user_id, password):
    with open('user_data.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['user_id', 'password'])
        csvwriter.writerow([user_id, password])

# read the CSV file and search for a password for a given user-id
def search_password(user_id):
    with open('user_data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # skip the header row
        next(csvreader)
        for row in csvreader:
            if row[0] == user_id:
                return row[1]
        return None

# example usage
user_id = input("Enter user id: ")
password = input("Enter password: ")
create_csv(user_id, password)
user_id = input("Enter user id to search ")
search_result = search_password(user_id)
if search_result:
    print("Password for user id", user_id, "is", search_result)
else:
    print("User id not found.")

