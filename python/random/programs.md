Karthik Nair | 3EA | 00229802021

# Random Module

### 1.  Write a program to generate 3 random integers between 100 and 999 which are divisible by 5.
```python

import random

for i in range(3):
    print(random.randrange(100, 999, 5))

```

### 2.  Write a program to generate 100 random lottery tickets (each lottery number must be 10 digits long) and pick two lucky tickets from it as a winner.
```python


import random

def lottery_generator(n):
    tickets=[]
    while len(tickets)!=n:
        ticket=random.randint(1000000000,9999999999)
        if ticket not in tickets:
            tickets.append(ticket)
        
    return tickets

def lucky_tickets(tickets, n):
    lucky_tickets=[]
    while len(lucky_tickets)!=n:
        lucky_ticket=random.choice(tickets)
        if lucky_ticket not in lucky_tickets:
            lucky_tickets.append(lucky_ticket)
    return lucky_tickets

tickets=lottery_generator(100)
print(f"Lucky tickets are {lucky_tickets(tickets,2)}") 

```

### 3. Write a program to generate random String of length entered by the user. String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol except single space.
### 
```python

import random
import string

def random_string(length):
    string0=""
    for i in range(length):
        string0+=random.choice(string.ascii_letters)
    return string0

length=int(input("Enter the length of the string: "))
print(random_string(length))

```

