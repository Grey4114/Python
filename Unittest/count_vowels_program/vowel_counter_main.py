"""
Author: Chris Caprio
Program: Count Vowels
Details:
Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum for each vowel found.

Notes: Main section of the vowel_counter.py script

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



