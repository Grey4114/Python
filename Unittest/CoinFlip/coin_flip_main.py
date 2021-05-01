"""
Author: Chris Caprio
Program: Coin Flip Simulation
Details:
    Write some code that simulates flipping a single coin however many times the user decides.
    The code should record the outcomes and count the number of tails and heads.
"""

# Froms & Imports
from coin_flip_functions import input_flips, flip_the_coin, show_results, play_again



# Function - This while loop runs all of th game functions
def main():
    playing = True
    while playing:
        flips = input_flips()
        flip_count = flip_the_coin(flips)
        show_results(flip_count)
        playing = play_again()


# Main - This runs the main function
if __name__ == "__main__":
    while True:
        print("\nWelcome to the Coin Flip Simulation")
        main()
        break