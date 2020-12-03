"""
Author: Chris Caprio
Program: Coin Flip Simulation
Details:
Write some code that simulates flipping a single coin however many times the user decides.  The code should record
the outcomes and count the number of tails and heads.

Notes:

"""

""" --- Froms & Imports --- """
import random
from collections import Counter

""" --- Global Variables and Settings --- """
playing = True
heads = 0   # Note this is not a counter, used as an identifier of heads
tails = 1   # Note this is not a counter, used as an identifier of tails


""" ---- FUNCTIONS --- """
# Create a random number generator(RNG)
# Gives either 0 or 1
def generate_number():
    return random.randrange(0, 2)


# Print coin flip results of each coin as it is flipped
def flip_results(flips):
    if flips == 0:
        print('Heads')
    else:
        print('Tails')


# Flips the coin and keeps list of the flips
def flip_the_coin(flips):
    for x in range(flips):
        number = generate_number()
        flip_results(number)
        flip_count.append(number)
    return flip_count


# Post total Head / Tails results
def show_results(flips, heads, tails):
    return f'{flips} Flips: {heads} Heads & {tails} Tails'


""" ---- MAIN SECTION --- """
# Starting while loop
while True:
    # Print opening statement
    print("\nWelcome to the Coin Flip Simulation")

    # Playing while loop
    while playing:
        flips = 0
        flip_count = []

        # Player inputs the flip amount and the input is checked if it is a number
        while True:
            try:
                flips = int(input("\nNumber of times to flip the coin: "))
            except ValueError:
                print("Error! That's not a number. Please try again.")
                continue
            break

        # Flip the coins, count the flips and print results
        flip_count = flip_the_coin(flips)
        coin_flips = Counter(flip_count)
        print(show_results(flips, coin_flips[heads], coin_flips[tails]))


        # Ask to play again
        while True:
            play_again = input("\nPlay Again (Y,N): ")
            if play_again.upper() == "Y":
                break

            elif play_again.upper() == "N":
                print(f"\nThanks for playing!!")
                playing = False
                break
            else:
                print("Please enter 'Y' or 'N'.")
    break
