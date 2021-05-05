"""
Author: Chris Caprio
Program: Pig Latin
Notes: Unittest script that tests the pig_latin_complex_functions.py script
"""

# Imports & Variables
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from pig_latin_complex_functions import opening_info, enter_text_string, convert_sentance, transform_word
from pig_latin_complex_functions import vowel_word, consonant_word, print_pig_latin, play_again


# TEST - check that the opening text has not changed and is being shown
class TestOpeningInfo(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_opening_text(self):
        opening_info()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Welcome to the Pig Latin Translator Program'
                                                        '\n\tHow the program works:'
                                                        '\n\tEnter a word or a sentence that does not contain any numbers or special characters'
                                                        '\n\tand the program will convert it into pig latin.')

    def tearDown(self):
        pass


# TEST - Input the text string and verify that it does not have any numbers or special characters
class TestEnterTextString(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    # todo - get mock to work with error text
    """
    # Enter nothing, returns an error
    @patch('builtins.input', return_value='')
    def test_input_noInput(self, mock_input):
        string = enter_text_string()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Error! Empty string, please try again')

    # Input a space, returns an error
    @patch('builtins.input', return_value=' ')
    def test_input_blankSpace(self, mock_input):
        string = enter_text_string()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Error! Empty string, please try again')

    # Input a word with a number, returns an error
    @patch('builtins.input', return_value='word5')
    def test_input_wordNumber(self, mock_input):
        string = enter_text_string()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Error! Contains numbers, please try again')
    """

    # Input a word, returns the word
    @patch('builtins.input', return_value='quick')
    def test_input_word(self, mock_input):
        string = enter_text_string()
        self.assertEqual(string, 'quick')

    # Input a sentance, return the sentance
    @patch('builtins.input', return_value='quick brown fox jumps over the lazy dog')
    def test_input_sentance(self, mock_input):
        string = enter_text_string()
        self.assertEqual(string, 'quick brown fox jumps over the lazy dog')


# TEST - check that a word/sentance is converted
class TestConvertSentance(unittest.TestCase):
    def test_convert_word(self):
        string = convert_sentance('quick')
        self.assertEqual(string, 'uickqay')

    def test_convert_sentance(self):
        string = convert_sentance('quick brown fox jumps over the lazy dog')
        self.assertEqual(string, 'uickqay ownbray oxfay umpsjay overway ethay azylay ogday')


# TEST - check that the word starts with a vowel and add 'way' to the end of the word
class TestTransformWord_Vowels(unittest.TestCase):
    def test_vowel_singleLetter_A(self):
        word = transform_word('a')
        self.assertEqual(word, 'away')

    def test_vowel_singleLetter_E(self):
        word = transform_word('e')
        self.assertEqual(word, 'eway')

    def test_vowel_singleLetter_I(self):
        word = transform_word('i')
        self.assertEqual(word, 'iway')

    def test_vowel_singleLetter_O(self):
        word = transform_word('o')
        self.assertEqual(word, 'oway')

    def test_vowel_singleLetter_U(self):
        word = transform_word('u')
        self.assertEqual(word, 'uway')

    def test_vowel_singleLetter_Y(self):
        word = transform_word('y')
        self.assertEqual(word, 'yway')

    def test_vowel_IN(self):
        word = transform_word('in')
        self.assertEqual(word, 'inway')

    def test_vowel_YET(self):
        word = transform_word('yet')
        self.assertEqual(word, 'yetway')

    def test_vowel_YOU(self):
        word = transform_word('you')
        self.assertEqual(word, 'youway')

    def test_vowel_OTHER(self):
        word = transform_word('other')
        self.assertEqual(word, 'otherway')


# TEST - check that the word starts with 1, 2 or more consonants
# then check the consonants are moved to the end and 'ay' is added
class TestTransformWord_Consonants(unittest.TestCase):
    def test_consonant_TO(self):
        word = transform_word('to')
        self.assertEqual(word, 'otay')

    def test_consonant_TIP(self):
        word = transform_word('tip')
        self.assertEqual(word, 'iptay')

    def test_consonant_THE(self):
        word = transform_word('the')
        self.assertEqual(word, 'ethay')

    def test_consonant_THIS(self):
        word = transform_word('this')
        self.assertEqual(word, 'isthay')

    def test_consonant_STRING(self):
        word = transform_word('string')
        self.assertEqual(word, 'ingstray')


# TEST - Check that the function adds 'way' to the end of the word or letter
class TestVowelWord(unittest.TestCase):
    def test_vowel_blankSpace(self):
        word = vowel_word(' ')
        self.assertEqual(word, ' way')

    def test_vowel_A(self):
        word = vowel_word('a')
        self.assertEqual(word, 'away')

    def test_vowel_E(self):
        word = vowel_word('e')
        self.assertEqual(word, 'eway')

    def test_vowel_I(self):
        word = vowel_word('i')
        self.assertEqual(word, 'iway')

    def test_vowel_O(self):
        word = vowel_word('o')
        self.assertEqual(word, 'oway')

    def test_vowel_U(self):
        word = vowel_word('u')
        self.assertEqual(word, 'uway')

    def test_vowel_Y(self):
        word = vowel_word('y')
        self.assertEqual(word, 'yway')

    def test_vowel_IN(self):
        word = vowel_word('in')
        self.assertEqual(word, 'inway')

    def test_vowel_YET(self):
        word = vowel_word('yet')
        self.assertEqual(word, 'yetway')

    def test_vowel_YOU(self):
        word = vowel_word('you')
        self.assertEqual(word, 'youway')

    def test_vowel_OTHER(self):
        word = vowel_word('other')
        self.assertEqual(word, 'otherway')


# TEST - check that the letter or letters are moved to the end of the word and 'ay' is added to the end
class TestConsonantWord(unittest.TestCase):
    def test_word_1(self):
        word = consonant_word('string', 1)
        self.assertEqual(word, 'tringsay')

    def test_word_2(self):
        word = consonant_word('string', 2)
        self.assertEqual(word, 'ringstay')

    def test_word_3(self):
        word = consonant_word('string', 3)
        self.assertEqual(word, 'ingstray')


# TEST - Check that the printed original and pig latin text is correct
class TestPrintPigLatin(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_print_vowelWord(self):
        print_pig_latin('other', 'otherway')
        self.assertEqual(sys.stdout.getvalue().strip(), 'Oringal: other'
                                                        '\n\tPig Latin: otherway')

    def test_print_consonantWord(self):
        print_pig_latin('word', 'ordway')
        self.assertEqual(sys.stdout.getvalue().strip(), 'Oringal: word'
                                                        '\n\tPig Latin: ordway')

    def test_print_sentance(self):
        print_pig_latin('you and I jump through the fire', 'youway andway iway umpjay oughthray ethay irefay')
        self.assertEqual(sys.stdout.getvalue().strip(), 'Oringal: you and I jump through the fire'
                                                        '\n\tPig Latin: youway andway iway umpjay oughthray ethay irefay')


# TEST - checks the play_again function
class TestPlayAgain(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    # User inputs 'y'
    @patch('builtins.input', return_value='y')
    def test_input_y(self, mock_input):
        play = play_again()
        self.assertEquals(play, True)

    # User inputs 'n'
    @patch('builtins.input', return_value='n')
    def test_input_n(self, mock_input):
        play = play_again()
        self.assertEquals(play, False)
        self.assertEqual(sys.stdout.getvalue().strip(), "Thanks for playing!!")

    # todo - get mock to work with error text
    """
    # User inputs 'a'
    @patch('builtins.input', return_value='a')
    def test_input_other_text(self, mock_input):
        play = play_again()
        self.assertEquals(play, False)

    # User inputs a number
    @patch('builtins.input', return_value=1)
    def test_input_number(self, mock_input):
        play = play_again()
        self.assertEquals(play, False)
    """
    def tearDown(self):
        pass


# Main - This runs all of the tests
if __name__ == '__main__':
    unittest.main()
