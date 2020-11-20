"""
Program: Change Return
Created: 11/17/2020
Updated: 11/20/2020
Script Type: Functions section only
Notes:
    The original script is change_return.py
    I have broken it into 2 scripts - return_change_main and return_change_functions to exapnd my skills in working
    with multiple connected scripts

"""

import random


""" --- VARIABLES --- """
# A list of product costs - Must be floats
purchase_prices = [0.99, 1.94, 2.84, 3.59, 4.12]
currency_dict = {0: 'Dollars', 1: 'Quarters', 2: 'Dimes', 3: 'Nickels', 4: 'Pennies'}


""" --- FUNCTIONS --- """
# Randomly choose product cost from list
def choose_random_price():
    pick = random.choice(purchase_prices)
    return pick


# Calculate that the payment is more then the purchase price
def check_the_payment(price, payment):
    if price > payment:
        print("Enter a dollar amount that is higher than the Purchase Price")
        return True
    else:
        return False


# Calculate differnce between cost and payment
def calc_difference(price, payment):
    return round(payment - price, 2)


# Break out change amounts
def calc_change(diff):
    if diff < 0:
        raise TypeError("Wrong data.  Requires a positve number. ")
    else:
        if diff > 1:
            dollars = int(diff)
            diff = round(diff - dollars, 2)
        else:
            dollars = 0

        if diff >= .25:
            quarters = int(diff / .25)
            diff = round(diff - (quarters * .25), 2)
        else:
            quarters = 0

        if diff >= .10:
            dimes = int(diff / .10)
            diff = round(diff - (dimes * .10), 2)
        else:
            dimes = 0

        if diff >= .05:
            nickels = int(diff / .05)
            diff = round(diff - (nickels * .05), 2)
        else:
            nickels = 0

        pennies = int(diff / .01)
        return dollars, quarters, dimes, nickels, pennies


# Prints the number of each bill/coin type
def show_change(diff, change):
    print(f"The Return Change for ${diff} is:")

    if isinstance(diff, float) or diff > 0:
        for x in range(0, 5):
            if change[x] > 0:
                print(f"\t{change[x]} {currency_dict[x]}")

    else:
        raise TypeError("Error! Incorrect info provided")


