"""
Author: Chris Caprio
Program: Coin Flip Simulation
Notes: Functions section of the coin_flip.py script
"""


""" --- Froms & Imports --- """
import random


""" --- VARIABLES --- """
flip_count = []


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





