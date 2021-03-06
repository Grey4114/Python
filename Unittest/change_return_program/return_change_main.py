"""
Author: Chris Caprio
Program: Change Return
Details:
The user enters a cost and then the amount of money given. The program will figure out the change and the number of
quarters, dimes, nickels, pennies needed for the change.

Notes: Main section of the change_return.py script

"""

from return_change_functions import choose_random_price, check_the_payment, calc_difference, calc_change, show_change
play = True

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

