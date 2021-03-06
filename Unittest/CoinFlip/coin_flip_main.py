"""
Author: Chris Caprio
Program: Coin Flip Simulation
Details:
    Write some code that simulates flipping a single coin however many times the user decides.
    The code should record the outcomes and count the number of tails and heads.

Note: Main section of the coin_flip.py script

"""

# Froms & Imports
import sys
from collections import Counter
from coin_flip_functions import flip_the_coin, show_results


# Global Variables and Settings
playing = True


# Starting while loop
while True:
    # Print opening statement
    print("\nWelcome to the Coin Flip Simulation")

    # Playing while loop
    while playing:
        flips = 0
        heads = 0  # Note this is not a counter, used as an identifier of heads
        tails = 1  # Note this is not a counter, used as an identifier of tails

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