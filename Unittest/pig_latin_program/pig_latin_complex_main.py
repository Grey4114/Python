"""
Author: Chris Caprio
Program: Pig Latin
Details:
    Pig Latin is a game of alterations played on the English language game.
    The user will be given the option of either converting a single word or sentence to pig latin.
    Word/Sentences with numbers and non-alphabetic characters will be rejected.
"""

# Imports & Variables
from pig_latin_complex_functions import opening_info, enter_text_string, convert_sentance, print_pig_latin, play_again


# Function - this while loops runs/controls all of the functions
def start():
    playing = True
    while playing:
        text_string = enter_text_string()
        pig_latin = convert_sentance(text_string)
        print_pig_latin(text_string, pig_latin)
        playing = play_again()


# Main - This while loop runs the start function
if __name__ == "__main__":
    while True:
        opening_info()
        start()
        break

