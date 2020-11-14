"""
Coin Flip Simulation
- Write some code that simulates flipping a single coin however many times the user decides.
The code should record the outcomes and count the number of tails and heads.

Script : Main script only
Created: 11/13/2020
Notes:
    The Main and Function sections are broken out into 2 scripts that connected together.
    I did this to practice using/connecting multiple scripts.
"""

# Froms & Imports
import sys
from collections import Counter
from CoinFlip import coin_flip_functions

# Global Variables and Settings
playing = True



# ---- MAIN SECTION
# Starting while loop
while True:
    # Print opening statement
    print("\nWelcome to the Coin Flip Simulation")

    # Create the coins and variables
    results = []
    heads = 0
    tails = 1
    flips = 0

    # Playing while loop
    while playing:
        player = coin_flip_functions.player_name()
        flips = coin_flip_functions.number_of_flips()

        for x in range(flips):
            number = coin_flip_functions.generate_number()
            results.append(number)
            flip_results = coin_flip_functions.flip_results(number)
            print(flip_results)

        coins_flips = Counter(results)
        print(coin_flip_functions.show_results(flips, coins_flips[heads], coins_flips[tails]))
        playing = False


    # Ask to play again
    play_again = input("Play Again (Y,N): ")
    if play_again.upper() == "Y":
        playing = True

    elif play_again.upper() == "N":
        print(f"\nThanks for playing {player}.")
        break
    else:
        print("Please enter 'Y' or 'N'.")
        continue
