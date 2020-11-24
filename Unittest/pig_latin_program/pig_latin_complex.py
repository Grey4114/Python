"""
Program: Pig Latin
Created: 11/22/2020 - 11/23/2020
Script Type:
    One script - this is a more complex version using a PigLatin class and streamlined functions
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
    Added the PigLatin class and cleaned up the code

"""

""" --- VARIABLES --- """
special = "!@#$%^&*()-+_=,.<>?:;[]{}/"
vowels = "aeiouy"
playing = True



""" --- CLASSES --- """
class PigLatin:
    def __init__(self, word):
        self.word = word

    # Vowel - slice the word and return pig latin word
    def vowel_word(self):
        return self.word + 'way'

    # Consonant - slice the word and return pig latin word
    def consonant_word(self):
        return self.word[1::] + self.word[0] + 'ay'

    # Two consonants - slice the word and return pig latin word
    def two_consonant_word(self):
        return self.word[2::] + self.word[0:2] + 'ay'

    # Three Consonant - slice the word and return pig latin word
    def three_consonant_word(self):
        return self.word[3::] + self.word[0:3] + 'ay'

    # This simple returns what the current word is
    def __str__(self):
        return f'The word that is being converted is: {self.word}'




""" --- FUNCTIONS --- """
# This checks the word and returns the pig latin version
def transform_word(word):
    word_in = word.lower()
    pl = PigLatin(word_in)
    word_type = check_word_type(word_in)

    if word_type == "v":
        return pl.vowel_word()
    elif word_type == "c":
        return pl.consonant_word()
    elif word_type == "c2":
        return pl.two_consonant_word()
    else:
        return pl.three_consonant_word()


# Word - Check if the word starts with a consonant(s)
def check_word_type(word):
    type = 0

    for v in vowels:
        for i, let in enumerate(word):
            if v == let:
                type = i - 1
                break

    if type == 1:
        word_type = 'v'
    elif type == 2:
        word_type = 'c'
    elif type == 3:
        word_type = 'c2'
    else:
        word_type = 'c3'

    return word_type


# Sentance - Transform each word and add into the sentance
def convert_sentance(sentance):
    sentance = sentance.split()
    new_sentance = []
    for word in sentance:
        pig_latin_word = transform_word(word)
        new_sentance.append(pig_latin_word)
        pig_latin_sentance = " ".join(new_sentance)
    return pig_latin_sentance


# Users choice transform the Word / Sentance into pig latin
def user_choice(choice):
    if choice == 'w':
        pig_latin_word = transform_word(word)
        print_pig_latin_word(word, pig_latin_word)
    else:
        pig_latin_sentance = convert_sentance(sentance)
        print_pig_latin_sentance(sentance, pig_latin_sentance)




# Print the orinal word and the pig latin word
def print_pig_latin_word(word, pig_latin_word):
    print(f'\n\t  Oringal Word: {word}\n\tPig Latin Word: {pig_latin_word}')


# Print the original sentance and the new pig latin sentance
def print_pig_latin_sentance(sentance, pig_latin_sentance):
    print(f'\n\t  Oringal Sentance: {sentance}\n\tPig Latin Sentance: {pig_latin_sentance}')




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

        # user_choice(choice)


        # Word / Sentance transform section
        if choice.lower() == 'w':
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

