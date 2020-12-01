"""
Program: Pig Latin
Created: 11/23/2020
Script Type:
    Functions Only - this is orinally from the pig_latin_complex script

Program Details:
    Pig Latin is a game of alterations played on the English language game.
    Read Wikipedia for more info. https://en.wikipedia.org/wiki/Pig_Latin

Notes:
    Broke the pig_latin_complex script into 3 scripts - main, function & class-  to improve skills of linking
    multiple scripts

    Made improvements over the original pig_latin_complex script

"""

""" --- IMPORTS --- """
from pig_latin_complex_class import PigLatin


""" --- VARIABLES --- """
vowels = ('aeiouy')

""" --- FUNCTIONS --- """
# Checks where the first vowel is and marks its position
def check_for_vowel(word_in):
    new_count = 5

    for v in vowels:
        count = word_in.find(v)
        if count < new_count and count >= 0:
            new_count = count

    return new_count


# This checks the word and returns the pig latin version
def transform_word(word):
    word_type = ""
    word_in = word.lower()
    pl = PigLatin(word_in)

    word_type = check_for_vowel(word_in)

    if word_type == 0:
        return pl.vowel_word()
    elif word_type == 1:
        return pl.consonant_word()
    elif word_type == 2:
        return pl.two_consonant_word()
    else:
        return pl.three_consonant_word()


# Sentnce - Transform each word and add into the sentance
def convert_sentance(sentance):
    sentance = sentance.split()
    new_sentance = []
    for word in sentance:
        pig_latin_word = transform_word(word)
        new_sentance.append(pig_latin_word)
        pig_latin_sentance = " ".join(new_sentance)
    return pig_latin_sentance


# Users choice transform the Word / Sentance into pig latin
def user_choice(choice, word, sentance):
    if choice.lower() == 'w':
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



