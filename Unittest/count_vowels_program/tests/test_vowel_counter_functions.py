"""
Author: Chris Caprio
Program: Count Vowels
Notes: Unittest script that tests the vowel_counter_functions.py script
"""

import sys
import unittest
from io import StringIO
from unittest.mock import patch
from vowel_counter_functions import opening_info, string_input, get_vowels, count_vowels, print_vowels, play_again
from vowel_counter_functions import vowels


# TEST - check that the opening text has not changed and is being shown
class TestOpeningInfo(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.open = opening_info()

    def test_opening_text(self):
        self.open
        self.assertEqual(sys.stdout.getvalue().strip(), 'Vowel Counter Program'
                                                        '\n\tEnter a string of words or letters'
                                                        '\n\tThe program will count the vowels and return the count for each vowel.')

    def tearDown(self):
        self.open = None


# TEST - check that the string that is input is returned
class TestStringInput(unittest.TestCase):
    # todo - get mock to work with error text
    """
    # Input nothing, just press Enter and returns  error
    @patch('builtins.input', return_value='')
    def test_enter_nothing(self, mock_input):
        self.assertEqual(self.string, '')
    """

    # Input a space, returns  a space
    @patch('builtins.input', return_value=' ')
    def test_input_blankSpace(self, mock_input):
        string = string_input()
        self.assertEqual(string, ' ')

    # Input 5, returns  5
    @patch('builtins.input', return_value=5)
    def test_input_oneNumber(self, mock_input):
        string = string_input()
        self.assertEqual(string, 5)

    # Input 'a', returns  'a'
    @patch('builtins.input', return_value='a')
    def test_input_oneVowel(self, mock_input):
        string = string_input()
        self.assertEqual(string, 'a')

    # Input 'b', returns  'b'
    @patch('builtins.input', return_value='b')
    def test_input_oneConsonent(self, mock_input):
        string = string_input()
        self.assertEqual(string, 'b')

    # Input &, returns  &
    @patch('builtins.input', return_value='&')
    def test_input_oneSpecailCharacter(self, mock_input):
        string = string_input()
        self.assertEqual(string, '&')

    # Input 'aeiouy', returns  'aeiouy'
    @patch('builtins.input', return_value='aeiouy')
    def test_input_allVowels(self, mock_input):
        string = string_input()
        self.assertEqual(string, 'aeiouy')

    # Input 'bcdfg', returns  'bcdfg'
    @patch('builtins.input', return_value='bcdfg')
    def test_input_allConsonants(self, mock_input):
        string = string_input()
        self.assertEqual(string, 'bcdfg')

    # Input 'The Quick Brown Fox Jumps Over The Lazy Dog', returns  'The Quick Brown Fox Jumps Over The Lazy Dog'
    @patch('builtins.input', return_value='The Quick Brown Fox Jumps Over The Lazy Dog')
    def test_input_sentanceWithSpaces(self, mock_input):
        string = string_input()
        self.assertEqual(string, 'The Quick Brown Fox Jumps Over The Lazy Dog')

    # Input ' Quick', returns  ' Quick'
    @patch('builtins.input', return_value=' Quick')
    def test_input_StartingSpace(self, mock_input):
        string = string_input()
        self.assertEqual(string, ' Quick')

    # Input 'qwer tyuio p[ ]5@#$afsg', returns 'qwer tyuio p[ ]5@#$afsg'
    @patch('builtins.input', return_value='qwer tyuio p[ ]5@#$afsg')
    def test_input_AlphaNumericSpecial(self, mock_input):
        string = string_input()
        self.assertEqual(string, 'qwer tyuio p[ ]5@#$afsg')


# TEST - checks that the function how many time each vowel appears in the sentence
class TestGetVowels(unittest.TestCase):
    def test_get_oneSpace(self,):
        v_count = get_vowels(" ", vowels)
        self.assertEqual(v_count, [])

    def test_get_oneNumber(self,):
        v_count = get_vowels('5', vowels)
        self.assertEqual(v_count, [])

    def test_get_oneVowel(self,):
        v_count = get_vowels("a", vowels)
        self.assertEqual(v_count, [('a', 1)])

    def test_get_oneConsonant(self,):
        v_count = get_vowels("b", vowels)
        self.assertEqual(v_count, [])

    def test_get_oneSpecial(self,):
        v_count = get_vowels("&", vowels)
        self.assertEqual(v_count, [])

    def test_get_allVowels(self,):
        v_count = get_vowels('aeiouy', vowels)
        self.assertEqual(v_count, [('a', 1), ('e', 1), ('i', 1), ('o', 1), ('u', 1), ('y', 1)])

    def test_get_allConsonants(self,):
        v_count = get_vowels("bcdfg", vowels)
        self.assertEqual(v_count, [])

    def test_get_oneVowelWord(self,):
        v_count = get_vowels("wind", vowels)
        self.assertEqual(v_count, [('i', 1)])

    def test_get_wordStartingSpace(self,):
        v_count = get_vowels(" wind", vowels)
        self.assertEqual(v_count, [('i', 1)])

    def test_get_setenceAlphaLower(self,):
        v_count = get_vowels('the quick brown fox jumps over the lazy dog', vowels)
        self.assertEqual(v_count, [('a', 1), ('e', 3), ('i', 1), ('o', 4), ('u', 2), ('y', 1)])

    def test_get_setenceAlphaUpper(self,):
        v_count = get_vowels('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', vowels)
        self.assertEqual(v_count, [('a', 1), ('e', 3), ('i', 1), ('o', 4), ('u', 2), ('y', 1)])

    def test_get_stringWithEverthing(self,):
        v_count = get_vowels('qwer tyuio p[ ]5@#$afsg', vowels)
        self.assertEqual(v_count, [('a', 1), ('e', 1), ('i', 1), ('o', 1), ('u', 1), ('y', 1)])


# TEST - count the total number of vowels in the string
class TestCountVowels(unittest.TestCase):
    def test_count_none(self,):
        tot_count = count_vowels([])
        self.assertEqual(tot_count, 0)

    def test_count_A(self,):
        tot_count = count_vowels([('a', 1)])
        self.assertEqual(tot_count, 1)

    def test_count_E(self,):
        tot_count = count_vowels([('e', 2)])
        self.assertEqual(tot_count, 2)

    def test_count_I(self,):
        tot_count = count_vowels([('i', 3)])
        self.assertEqual(tot_count, 3)

    def test_count_O(self,):
        tot_count = count_vowels([('o', 4)])
        self.assertEqual(tot_count, 4)

    def test_count_U(self,):
        tot_count = count_vowels([('u', 5)])
        self.assertEqual(tot_count, 5)

    def test_count_Y(self,):
        tot_count = count_vowels([('y', 6)])
        self.assertEqual(tot_count, 6)

    def test_count_allVowels(self,):
        tot_count = count_vowels([('a', 1), ('e', 1), ('i', 1), ('o', 1), ('u', 1), ('y', 1)])
        self.assertEqual(tot_count, 6)

    def test_count_allVowels_HighCount(self,):
        tot_count = count_vowels([('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5), ('y', 6)])
        self.assertEqual(tot_count, 21)

    def test_count_someVowels(self,):
        tot_count = count_vowels([('a', 1), ('i', 2), ('u', 3)])
        self.assertEqual(tot_count, 6)


# TEST - print the list of vowels, counts and the total count
class TestPrintVowels(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_print_none(self):
        print_vowels([],0)
        self.assertEqual(sys.stdout.getvalue().strip(), "List of vowels in the string"
                                                        "\nvowel : count"
                                                        "\n\nTotal vowels: 0")

    def test_print_A(self):
        print_vowels([('a', 1)],1)
        self.assertEqual(sys.stdout.getvalue().strip(), "List of vowels in the string"
                                                        "\nvowel : count"
                                                        "\n\ta : 1"
                                                        "\nTotal vowels: 1")

    def test_print_E(self):
        print_vowels([('e', 1)],1)
        self.assertEqual(sys.stdout.getvalue().strip(), "List of vowels in the string"
                                                        "\nvowel : count"
                                                        "\n\te : 1"
                                                        "\nTotal vowels: 1")

    def test_print_I(self):
        print_vowels([('i', 1)],1)
        self.assertEqual(sys.stdout.getvalue().strip(), "List of vowels in the string"
                                                        "\nvowel : count"
                                                        "\n\ti : 1"
                                                        "\nTotal vowels: 1")

    def test_print_O(self):
        print_vowels([('o', 1)],1)
        self.assertEqual(sys.stdout.getvalue().strip(), "List of vowels in the string"
                                                        "\nvowel : count"
                                                        "\n\to : 1"
                                                        "\nTotal vowels: 1")

    def test_print_U(self):
        print_vowels([('u', 1)],1)
        self.assertEqual(sys.stdout.getvalue().strip(), "List of vowels in the string"
                                                        "\nvowel : count"
                                                        "\n\tu : 1"
                                                        "\nTotal vowels: 1")

    def test_print_Y(self):
        print_vowels([('y', 1)],1)
        self.assertEqual(sys.stdout.getvalue().strip(), "List of vowels in the string"
                                                        "\nvowel : count"
                                                        "\n\ty : 1"
                                                        "\nTotal vowels: 1")

    def test_print_All(self):
        print_vowels([('a', 1), ('e', 1), ('i', 1), ('o', 1), ('u', 1), ('y', 1)],6)
        self.assertEqual(sys.stdout.getvalue().strip(), "List of vowels in the string"
                                                        "\nvowel : count"
                                                        "\n\ta : 1"
                                                        "\n\te : 1"
                                                        "\n\ti : 1"
                                                        "\n\to : 1"
                                                        "\n\tu : 1"
                                                        "\n\ty : 1"
                                                        "\nTotal vowels: 6")

    def test_print_AIU(self):
        print_vowels([('a', 1), ('i', 2), ('u', 3)],6)
        self.assertEqual(sys.stdout.getvalue().strip(), "List of vowels in the string"
                                                        "\nvowel : count"
                                                        "\n\ta : 1"
                                                        "\n\ti : 2"
                                                        "\n\tu : 3"
                                                        "\nTotal vowels: 6")

    def test_print_All_HighCount(self):
        print_vowels([('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5), ('y', 6)], 21)
        self.assertEqual(sys.stdout.getvalue().strip(), "List of vowels in the string"
                                                        "\nvowel : count"
                                                        "\n\ta : 1"
                                                        "\n\te : 2"
                                                        "\n\ti : 3"
                                                        "\n\to : 4"
                                                        "\n\tu : 5"
                                                        "\n\ty : 6"
                                                        "\nTotal vowels: 21")

    def tearDown(self):
        pass


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
