"""
Program: Pig Latin
Created: 11/23/2020
Script Type:
    Functions Only - this is orinally from the pig_latin_complex script

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
from pig_latin_complex_class import PigLatin


""" --- VARIABLES --- """
vowels = "aeiouy"



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
                type = i
                break

    if type == 0:
        word_type = 'v'
    elif type == 1:
        word_type = 'c'
    elif type == 2:
        word_type = 'c2'
    else:
        word_type = 'c3'

    return word_type


# Sentnce - Transform each word and add into the sentance
def convert_sentance(sentance):
    sentance = sentance.split()
    new_sentance = []
    for word in sentance:
        pig_latin_word = transform_word(word)
        new_sentance.append(pig_latin_word)
        pig_latin_sentance = " ".join(new_sentance)
    return pig_latin_sentance


# Print the orinal word and the pig latin word
def print_pig_latin_word(word, pig_latin_word):
    print(f'\n\t  Oringal Word: {word}\n\tPig Latin Word: {pig_latin_word}')


# Print the original sentance and the new pig latin sentance
def print_pig_latin_sentance(sentance, pig_latin_sentance):
    print(f'\n\t  Oringal Sentance: {sentance}\n\tPig Latin Sentance: {pig_latin_sentance}')


