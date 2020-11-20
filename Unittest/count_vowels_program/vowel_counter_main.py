"""
Program: Count Vowels
Created: 11/19/2020
Updated:
Script Type: Main Section only
Project Source:
    Pierian Data's Complete Python 3 Bootcamp Projects List
    https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/18-Milestone%20Project%20-%203/02-Final%20Capstone%20Project%20Ideas.ipynb

Program Details:
    Enter a string and the program counts the number of vowels in the text.
    For added complexity have it report a sum of each vowel found.

Notes:
    The vowel_counter script was split into the 2 scripts, vowel_counter_main and vowel_counter_functions
    to test working with mutiple connected script.
"""

from vowel_counter_functions import lower_the_string, slice_the_string, count_vowels, print_vowel_count
vowels = ('a', 'e', 'i', 'o', 'u', 'y')

""" --- MAIN --- """
# Main > Intro & Rules > Enter string > Check string > count vowels > show results > play again
# Starting/Main loop
while True:
    print('\nWelcome to the Vowel Counter program')
    print('\tHow the program works:')
    print('\tEnter a string of words or letters')
    print('\tThe program will count the vowels and return the count for each vowel.')
    input('Press Enter to continue')

    # Input string loop
    while True:
        try:
            start_string = input('\nEnter in a word, sentence or string: ')
            if not start_string:
                raise ValueError('\tError! Empty string, please try again')
        except ValueError as e:
            print(e)
            continue

        # Exits string loop
        break

    new_string = lower_the_string(start_string)
    slice_string = slice_the_string(new_string)
    vowel_count = count_vowels(slice_string, vowels)
    print_vowel_count(vowel_count)

    # Exit Main loop
    break



