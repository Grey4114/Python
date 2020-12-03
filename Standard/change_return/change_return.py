"""
Author: Chris Caprio
Program: Change Return Program
Details:
The user enters a cost and then the amount of money given. The program will figure out the change and the number
of quarters, dimes, nickels, pennies needed for the change.

Notes:
Adjusting the orinal parameters so that the user is shown a purchase amount and then can enter a integer for payment.
Then the program will calculate the change - Dollar, quarters, dimes, nickels & pennies.
"""

import random


""" --- VARIABLES --- """
# A list of product costs - Must be floats
purchase_prices = [0.99, 1.94, 2.84, 3.59, 4.12]
currency_dict = {0: 'Dollars', 1: 'Quarters', 2: 'Dimes', 3: 'Nickels', 4: 'Pennies'}
play = True



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
        raise TypeError("Wrong input data. Please make sure that everything is a number. ")
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
    if isinstance(diff, float):
        for x in range(0, 5):
            if change[x] > 0:
                print(f"\t{change[x]} {currency_dict[x]}")

    else:
        raise TypeError("Error! Incorrect info provided")


""" --- MAIN PROGRAM --- """
while True:
    print("\nWelcome to the Change Return program.")
    print("How the program works:")
    print("\t1) The player will be shown a Purchase Price")
    print("\t2) The Player will be asked to input a Payment amount.")
    print("\t3) The return change will be shown.")

    while True:
        price = choose_random_price()
        print(f'\nThe Purchase Price is ${price}.')

        while play:
            try:
                payment = int(input("Enter the Payment dollar amount: $"))
            except ValueError:
                print("Whoops! That's not a whole dollar amount. Please try again.")
                continue
            else:
                play = check_the_payment(price, payment)
        break

    diff = calc_difference(price, payment)
    change = calc_change(diff)
    show_change(diff, change)

    break

