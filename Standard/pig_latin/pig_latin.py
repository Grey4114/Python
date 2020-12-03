"""
Author: Chris Caprio
Program: Pig Latin
Details:
    Pig Latin is a game of alterations played on the English language game.
    The user will be given the option of either converting a single word or sentence into pig latin.
    Word/Sentences with numbers and non-alphabetic characters will be rejected.

Notes: This is a simple first pass / brute force version of the program.


"""


""" --- VARIABLES --- """
special = "!@#$%^&*()-+_=,.<>?:;[]{}/"
vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"
playing = True


""" --- FUNCTIONS --- """
# This checks the word and returns the pig latin version
def transform_word(word):
    word = word.lower()
    word_type = check_if_vowel(word)

    if word_type == "v":
        pig_latin = vowel_word(word)
        return pig_latin

    else:
        word_type = check_if_consonant(word)
        if word_type == "c":
            pig_latin = consonant_word(word)
            return pig_latin
        elif word_type == "c2":
            pig_latin = two_consonant_word(word)
            return pig_latin
        else:
            pig_latin = three_consonant_word(word)
            return pig_latin


# Word - Check if the word starts with a vowel
def check_if_vowel(word):
    for v in vowels:
        if word[0] == v:
            word_type = 'v'
            return word_type


# Word - Check if the word starts with a consonant(s)
def check_if_consonant(word):
    count = 0

    # Verify if word is a single consonant
    for a in consonants:
        if word[0] == a:
            word_type = 'c'
            count += 1
            break

    # Verify if word has two consonants
    if count == 1:
        for b in consonants:
            if word[1] == b:
                word_type = 'c2'
                count += 1
                break

    # Verify if word has three consonants
    if count == 2:
        for c in consonants:
            if word[2] == c:
                word_type = 'c3'
                break

    return word_type


# Vowel - slice the word and return pig latin word
def vowel_word(word):
    pig_latin = word + 'way'
    return pig_latin


# Consonant - slice the word and return pig latin word
def consonant_word(word):
    pig_latin = word[1::] + word[0] + 'ay'
    return pig_latin


# Two consonants - slice the word and return pig latin word
def two_consonant_word(word):
    pig_latin = word[2::] + word[0:2] + 'ay'
    return pig_latin


# Three Consonant - slice the word and return pig latin word
def three_consonant_word(word):
    pig_latin = word[3::] + word[0:3] + 'ay'
    return pig_latin


# Sentance - Slice up the sentence
def sentance_slice(sentance):
    new_sentance = sentance.split()
    return new_sentance

# Sentnce - Transform each word and add into the sentance
def convert_sentance(sentance):
    new_sentance = []
    for word in sentance:
        pig_latin = transform_word(word)
        new_sentance.append(pig_latin)
        pig_latin_sentance = " ".join(new_sentance)
    return pig_latin_sentance


# Print the orinal word and the pig latin word
def print_pig_latin_word(word, pig_latin):
    print(f'\n\t  Oringal Word: {word}\n\tPig Latin Word: {pig_latin}')


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
        pig_latin = ""
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
            pig_latin = transform_word(word)
            print_pig_latin_word(word, pig_latin)

        else:
            new_sentance = sentance_slice(sentance)
            pig_latin_sentance = convert_sentance(new_sentance)
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

