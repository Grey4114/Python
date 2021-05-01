"""
Author: Chris Caprio
Program: Change Return
Details:
The user enters a cost and then the amount of money given. The program will figure out the change and the number of
quarters, dimes, nickels, pennies needed for the change.

Notes: Main section of the change_return.py script

"""
# Imports & Variables
from return_change_functions import opening_info, choose_random_price, enter_payment, calc_difference
from return_change_functions import calc_change, print_results, play_again

# A list of product costs - Must be floats
prices = [0.99, 1.94, 2.84, 3.59, 4.12]


# Main while loop that runs all of the functions
def main():
    playing = True
    while playing:
        price = choose_random_price(prices)
        print(f'\nThe Purchase Price is ${price}.')
        payment = enter_payment(price)
        diff = calc_difference(price, payment)
        results = calc_change(diff)
        print_results(diff, results)
        playing = play_again()



# Calls the main() function
if __name__ == "__main__":
    payment = 0
    opening_info()
    main()


