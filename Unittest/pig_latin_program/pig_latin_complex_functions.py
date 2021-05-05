"""
Author: Chris Caprio
Program: Pig Latin - Functions
"""

# Imports and Variables
special = "!@#$%^&*()-+_=,.<>?:;[]{}/"
vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"


# Function - Applications opening/start up info
def opening_info():  # opening_info
    print('\nWelcome to the Pig Latin Translator Program')
    print('\tHow the program works:')
    print('\tEnter a word or a sentence that does not contain any numbers or special characters')
    print('\tand the program will convert it into pig latin.')


# Function - User enters a word or a sentence
def enter_text_string():
    text_string = ""
    while True:
        try:
            text_string = input('\nEnter a word or a sentance: ')
            if not text_string:
                raise ValueError('\tError! Empty string, please try again')
            elif any(a.isdigit() for a in text_string):
                raise ValueError('\tError! Contains numbers, please try again')
            elif any(sc in special for sc in text_string):
                raise ValueError('\tError! Contains special characters, please try again')
        except ValueError as e:
            print(e)
            continue
        break
    return text_string


# Function - Transform each word into a pig latin word
def convert_sentance(text_string):
    newString = text_string.split()
    return " ".join([transform_word(word) for word in newString])


# This checks the word and returns the pig latin version
def transform_word(word):
    word = word.lower()
    if [True for v in vowels if word[0] == v]:
        return vowel_word(word)
    elif word[0] in consonants and word[1] in consonants and word[2] in consonants:
        return consonant_word(word, 3)
    elif word[0] in consonants and word[1] in consonants:
        return consonant_word(word, 2)
    else:
        return consonant_word(word, 1)


# Function - Vowel - first letter is a vowel, return pig latin word
def vowel_word(word):
    return word + 'way'


# Function - Consonant - first letter is a consonant, return pig latin word
def consonant_word(word, n):
    return word[n::] + word[0:n] + 'ay'


# Function - Print the original sentance and the new pig latin sentance
def print_pig_latin(text_string, pig_latin):
    print(f'\n\tOringal: {text_string}\n\tPig Latin: {pig_latin}')


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

