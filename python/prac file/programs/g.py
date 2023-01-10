"""Write a program to generate 100 unique random lottery tickets
 (each lottery number must be 10 digits long) and 
pick two lucky tickets from it as a winner.
 Use random module."""

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
