"""
Program: Change Return
Created: 11/17/2020
Script Type: Main section only
Notes:
    The original script is change_return.py
    I have broken it into 2 scripts - return_change_main and return_change_functions to exapnd my skills in working
    with multiple connected scripts

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

