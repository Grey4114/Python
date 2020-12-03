"""
Author: Chris Caprio
Program: Pig Latin
Notes: Class section of the pig_latin_complex.py script

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