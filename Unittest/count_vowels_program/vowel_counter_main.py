"""
Author: Chris Caprio
Program: Count Vowels - main
Details:
Enter a string and the program counts the number of vowels in the text.
"""

# Imports and Variables
from vowel_counter_functions import opening_info, string_input, get_vowels, count_vowels, print_vowels, play_again
from vowel_counter_functions import vowels


# Function - this while loops runs/controls all of the functions
def start():
    playing = True
    while playing:
        start_string = string_input()
        in_string = get_vowels(start_string, vowels)
        vowel_count = count_vowels(in_string)
        print_vowels(in_string, vowel_count)
        playing = play_again()


# Main - This while loop runs the start function
if __name__ == "__main__":
    while True:
        opening_info()
        start()
        break






