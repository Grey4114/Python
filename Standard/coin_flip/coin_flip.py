"""
Author: Chris Caprio
Program: Coin Flip Simulation
Details:
Write some code that simulates flipping a single coin however many times the user decides.  The code should record
the outcomes and count the number of tails and heads.
"""

# Froms & Imports & Variables
import random
from collections import Counter


# Function - Player inputs the flip amount and the input is checked if it is a number
def start():
    flips = 0
    while True:
        try:
            flips = int(input("\nNumber of times to flip the coin: "))
        except ValueError:
            print("Error! That's not a number. Please try again.")
            continue
        break
    return flips


# Function - Flips the coin and returns a list of the flips - returns 0's or 1's
def flip_the_coin(flips):
    return [random.randrange(0, 2) for x in range(flips)]


# Function - Post total Head / Tails results
def show_results(flipCount):
    countFlips = Counter(flipCount)
    coin = {0: 'Heads', 1: 'Tails'}
    print(*[coin[n] for n in flipCount], sep="\n")  # Prints out each coin flip
    return f'{flips} Flips: {countFlips[0]} Heads & {countFlips[1]} Tails'


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

    while True:
        print("\nWelcome to the Coin Flip Simulation")

        while playing:
            flips = start()
            flip_count = flip_the_coin(flips)
            print(show_results(flip_count))
            playing = play_again()
        break

