"""
Author: Chris Caprio
Program: Change Return Program
Details:
The user enters a cost and then the amount of money given. The program will figure out the change and the number
of quarters, dimes, nickels, pennies needed for the change.
"""

# Froms, Imports & Variables
import random


# A list of product costs - Must be floats
prices = [0.99, 1.94, 2.84, 3.59, 4.12]
currency_dict = {0: 'Dollars', 1: 'Quarters', 2: 'Dimes', 3: 'Nickels', 4: 'Pennies'}


# Function - Prints the title and info
def opening_info():
    print("\nWelcome to the Change Return program.")
    print("\t1) The player will be shown a Purchase Price")
    print("\t2) The Player will be asked to input a Payment amount.")
    print("\t3) The return change will be shown.")


# Function - Randomly choose product cost from list
def choose_random_price(prices):
    return random.choice(prices)


# Function - Player enters a payment amounts
def enter_payment(price):
    check = True
    amount = 0
    while check:
        try:
            amount = int(input("Enter the Payment dollar amount: $"))
        except ValueError:
            print("Whoops! That's not a whole dollar amount. Please try again.")
            continue
        else:
            if price > amount:
                print("Enter a dollar amount that is higher than the Purchase Price")
                check = True
            else:
                check = False
    return amount


# Function - Calculate differnce between cost and payment
def calc_difference(price, payment):
    return round(payment - price, 2)


# Function - Break out change amounts
def calc_change(diff):
    money = [100, 25, 10, 5, 1]
    newDiff = round(diff*100)
    results = [0] * len(money)
    new = newDiff
    for index, coin in enumerate(money):
        results[index], new = divmod(new, coin)
    return results


# Function - Prints the number of each bill/coin type
def print_results(diff, results):
    print(f"\nThe Return Change is ${diff}:")
    print(*[f'{coin} : {currency_dict[index]}' for index, coin in enumerate(results) if coin > 0], sep='\n')


# Function - Asks the player to play again - Player Input
def play_again():
    while True:
        play_again = input("\nPlay Again (Y,N): ")
        if play_again.upper() == "Y":
            return True
        elif play_again.upper() == "N":
            print("\nThanks for playing!!")
            return False
        else:
            print("Please enter 'Y' or 'N'.")


# Main - This area runs all of the functions
if __name__ == "__main__":
    playing = True
    payment = 0
    opening_info()

    while playing:
        price = choose_random_price(prices)
        print(f'\nThe Purchase Price is ${price}.')
        payment = enter_payment(price)
        diff = calc_difference(price, payment)
        results = calc_change(diff)
        print_results(diff, results)
        playing = play_again()


