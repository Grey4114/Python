"""
Program: test_pig_latin_complex_class
Created: 11/23/2020
Script Type: Unittest script
Program Details:
    This script is designed to test the pig_latin_complex_class script

Notes:

"""

""" --- IMPORTS ---"""
import unittest
import sys
from io import StringIO
from pig_latin_complex_class import PigLatin


""" --- TEST CASES --- """
class TestPigLatin_Class(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.piglatin_vowel = PigLatin("are")
        self.piglatin_one_con = PigLatin("sure")
        self.piglatin_two_con = PigLatin("chuck")
        self.piglatin_three_con = PigLatin("strange")

    def test_vowel(self):
        check = self.piglatin_vowel.vowel_word()
        self.assertEqual(check, 'areway')

    def test_one_consonant(self):
        check = self.piglatin_one_con.consonant_word()
        self.assertEqual(check, 'uresay')

    def test_two_consonant(self):
        check = self.piglatin_two_con.two_consonant_word()
        self.assertEqual(check, 'uckchay')

    def test_three_consonant(self):
        check = self.piglatin_three_con.three_consonant_word()
        self.assertEqual(check, 'angestray')

    def test_word_vowel(self):
        print(self.piglatin_vowel)
        self.assertEqual(sys.stdout.getvalue().strip(), "The word that is being converted is: are")

    def test_word_one_consonant(self):
        print(self.piglatin_one_con)
        self.assertEqual(sys.stdout.getvalue().strip(), "The word that is being converted is: sure")

    def test_word_two_consonant(self):
        print(self.piglatin_two_con)
        self.assertEqual(sys.stdout.getvalue().strip(), "The word that is being converted is: chuck")

    def test_word_three_consonant(self):
        print(self.piglatin_three_con)
        self.assertEqual(sys.stdout.getvalue().strip(), "The word that is being converted is: strange")

    def tearDown(self):
        self.piglatin_vowel = None
        self.piglatin_one_con = None
        self.piglatin_two_con = None
        self.piglatin_three_con = None

if __name__ == '__main__':
    unittest.main()
