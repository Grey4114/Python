"""
Author: Chris Caprio
Program: Pig Latin
Details:
    Pig Latin is a game of alterations played on the English language game.
    The user will be given the option of either converting a single word or sentence to pig latin.
    Word/Sentences with numbers and non-alphabetic characters will be rejected.

Notes: Main section of the pig_latin_complex.py script
"""

""" --- IMPORTS --- """
from pig_latin_complex_functions import user_choice


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
        choice = ""
        word = ""
        sentance = ""
        pig_latin_word = ""
        pig_latin_sentance = ""

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

        # Runs the function that transform the Word / Sentance into pig latin
        user_choice(choice, word, sentance)

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
