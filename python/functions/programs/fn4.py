""" Let's use functions to calculate your trip's costs:
        a. Define a function called hotel_cost with one argument nights as input. The hotel costs $140 per night. So, the function hotel_cost should return 140 * nights.
        b. Define a function called plane_ride_cost that takes a string, city, as input. The function should return a different price depending on the location. Below are the valid destinations and their corresponding round-trip prices.
"Charlotte": 183
"Tampa": 220
"Pittsburgh": 222
"Los Angeles": 475
        c. Below your existing code, define a function called rental_car_cost with an argument called days. Calculate the cost of renting the car: Every day you rent the car costs $40.(cost=40*days) if you rent the car for 7 or more days, you get $50 off your total(cost-=50). Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. You cannot get both of the above discounts. Return that cost.
        d. Then, define a function called trip_cost that takes two arguments, city and days. Have your function return the sum of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.
        e. Modify your trip_cost function definion. Add a third argument, spending_money. Modify what the trip_cost function does. Add the variable `spending_money to the sum that it returns.
"""

def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return "Invalid destination"

def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


print(trip_cost("Los Angeles", 5, 1000))
