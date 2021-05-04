"""
Author: Chris Caprio
Program: Count Vowels - functions
"""

# Imports and Variables
from collections import Counter
vowels = ('a', 'e', 'i', 'o', 'u', 'y')


# Function - Prints the title and app info
def opening_info():
    print('\nVowel Counter Program')
    print('\tEnter a string of words or letters')
    print('\tThe program will count the vowels and return the count for each vowel.')


# Function - Player enters the string
def string_input():
    start_string = ""
    while True:
        try:
            start_string = input('\nEnter in a word, sentence or string: ')
            if not start_string:
                raise ValueError('\tError! Nothing entered, please try again')
        except ValueError as e:
            print(e)
            continue
        break  # Exits the loop
    return start_string


# Function - Counts the vowels
def get_vowels(start_string, vowels):
    countLetters = Counter(start_string.lower().replace('', ' '))
    return [(l, countLetters[l]) for l in vowels if countLetters[l] > 0]


# Function - Counts all of the vowels in the string
def count_vowels(in_string):
    return sum([x[1] for x in in_string])


# Function - Prints the list of vowels
def print_vowels(in_string, vowel_count):
    print("\nList of vowels in the string")
    print("vowel : count")
    print(*[f"\t{x[0]} : {x[1]}" for x in in_string], sep="\n")
    print(f"Total vowels: {vowel_count}")


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



