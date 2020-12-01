"""
Program: Pig Latin
Created: 11/23/2020
Script Type:
    Class Only - this is orinally from the pig_latin_complex script

Program Details:
    Pig Latin is a game of alterations played on the English language game.
    Read Wikipedia for more info. https://en.wikipedia.org/wiki/Pig_Latin

Notes:
    Broke the pig_latin_complex script into 3 scripts - main, function & class-  to improve skills of linking
    multiple scripts

"""

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

    # This simply returns what the current word is
    def __str__(self):
        return f'The word that is being converted is: {self.word}'


p = PigLatin('are')
p