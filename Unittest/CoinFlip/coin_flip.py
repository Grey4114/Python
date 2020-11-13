"""
Coin Flip Simulation
- Write some code that simulates flipping a single coin however many times the user decides.
The code should record the outcomes and count the number of tails and heads.

Script : All in one Coin Flip script
Created: 11/11/2020 - 11/12/2020

Notes:
    This is the original all in one Coin Flip script.  The Main and Function sections are broken out into 2 additional
    scripts that work together the same as this script.  I did this to practice using/connecting multiple scripts.
"""

# Froms & Imports
import random
from collections import Counter

# Global Variables and Settings
playing = True


# ----- FUNCTIONS
# Input a Player Name
def player_name():
    player = input("Enter your name: ")
    return player


# Ask player number of times to flip coin
def number_of_flips():
    while True:
        try:
            flips = int(input("Number of times to flip the coin: "))
        except:
            print("Whoops! That's not a number. Please try again.")
            continue
        break
    return flips


# Create a random number generator(RNG)
# Gives either 0 or 1
def generate_number():
    return random.randrange(0, 2)


# Print coin flip results of each coin as it is flipped
def flip_results(flips):
    if flips == 0:
        return 'Heads'
    else:
        return 'Tails'


# Post total Head / Tails results
def show_results(flips, heads, tails):
    return f'\n{flips} Flips: {heads} Heads & {tails} Tails'


# ---- MAIN SECTION
# Create main section
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
        player = player_name()
        flips = number_of_flips()

        for x in range(flips):
            number = generate_number()
            results.append(number)
            print(flip_results(number))

        coins_flips = Counter(results)
        print(show_results(flips, coins_flips[heads], coins_flips[tails]))
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


