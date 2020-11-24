"""
Program: Pig Latin
Created: 11/23/2020
Script Type:
    Main Only - this is orinally from the pig_latin_complex script

Program Details:
    Pig Latin is a game of alterations played on the English language game.
    Read Wikipedia for more info. https://en.wikipedia.org/wiki/Pig_Latin

Program Rules:
    The user will be given the option of either converting a single word or sentence to pig latin.
    Word/Sentences with numbers and non-alphabetic characters will be rejected.

    Words that begin with consonant sounds, all letters before the initial vowel are placed at the end of
    the word and "ay" is added.
    Examples are:
    "banana" = "ananabay"
    "string" = "ingstray"
    "trash" = "ashtray"
    "me" = "emay"

    Words that begin with vowel sounds, the vowel is left alone and 'way' is added to the end of the word.
    Examples are:
    "eat" = "eatyay"
    "omelet" = "omeletay"
    "I"= "Iyay"

Notes:
    Broke the pig_latin_complex script into 3 scripts - main, function & class-  to improve skills of linking
    multiple scripts

"""

""" --- IMPORTS --- """
from pig_latin_complex_functions import transform_word, convert_sentance, print_pig_latin_word, print_pig_latin_sentance


""" --- VARIABLES --- """
special = "!@#$%^&*()-+_=,.<>?:;[]{}/"
playing = True


""" --- MAIN --- """
# Main - Intro > Enter Word/Sentance > Check Word/Sentance > Print converted Word/Sentance > Play again
# START - Main loop
while True:
    print('\nWelcome to the Pig Latin Translator Program')
    print('\tHow the program works:')
    print('\tEnter a word or a sentence that does not contain any numbers or special characters')
    print('\tand the program will convert it into pig latin.')
    input('Press ENTER to continue')

    # START - Playing loop
    while playing:
        word_type = ""
        choice = ""
        word = ""
        sentance = []
        pig_latin_word = ""
        pig_latin_sentance = []

        # START - Choice loop
        while True:
            try:
                choice = input('\nEnter a (W) word or a (S) sentance: ')
                if choice.lower() != 'w' and choice.lower() != 's':
                    raise ValueError('\tError! Pleas try again. Enter "w" or "s" only')
            except ValueError as e:
                print(e)
                continue
            # END - Choice loop
            break


        # START - Word / Sentance loop
        while True:
            if choice.lower() == 'w':
                # Input Word - check that it is one word, no numbers, spaces or special characters
                try:
                    word = input('Enter a word: ')
                    if not word:
                        raise ValueError('\tError! Empty string, please try again')
                    elif any(not w.isalpha() for w in word):
                        raise ValueError('\tError! Contains numbers, spaces or special characters, please try again')
                except ValueError as e:
                    print(e)
                    continue

            else:
                # Input Sentance - check that it contains no numbers or special characters
                try:
                    sentance = input('Enter a sentance: ')
                    if not sentance:
                        raise ValueError('\tError! Empty string, please try again')
                    elif any(s.isdigit() for s in sentance):
                        raise ValueError('\tError! Contains numbers, please try again')
                    elif any(sc in special for sc in sentance):
                        raise ValueError('\tError! Contains special characters, please try again')
                except ValueError as e:
                    print(e)
                    continue

            # END - Word / Sentance loop
            break


        # Word / Sentance transform section
        if choice == 'w':
            pig_latin_word = transform_word(word)
            print_pig_latin_word(word, pig_latin_word)
        else:
            pig_latin_sentance = convert_sentance(sentance)
            print_pig_latin_sentance(sentance, pig_latin_sentance)


        # START - Play again loop
        while True:
            play_again = input("\nPlay Again (Y,N): ")
            if play_again.upper() == "Y":
                break
            elif play_again.upper() == "N":
                print(f"\nThanks for playing!!")
                playing = False
                break
            else:
                print("Please enter 'Y' or 'N'.")

    # END - Main loop
    break
