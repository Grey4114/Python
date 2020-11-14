"""
Coin Flip Simulation
- Write some code that simulates flipping a single coin however many times the user decides.
The code should record the outcomes and count the number of tails and heads.

Script : Functions only script
Created: 11/13/2020
Notes:
    The Main and Function sections are broken out into 2 scripts that are connected together.
    I did this to practice using/connecting multiple scripts.
"""


# Froms & Imports
import random


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





