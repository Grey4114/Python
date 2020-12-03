"""
Author: Chris Caprio
Program: Count Vowels
Notes: Unittest script that tests the vowel_counter_functions.py script
"""

import sys
import unittest
from io import StringIO
from vowel_counter_functions import lower_the_string, slice_the_string, count_vowels, print_vowel_count

# Tests the lower_the_string function
class TestLowerString(unittest.TestCase):
    def test_lower_all_caps(self):
        lower = lower_the_string('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')
        self.assertEqual(lower, 'the quick brown fox jumps over the lazy dog')

    def test_lower_all_lower(self):
        lower = lower_the_string('the quick brown fox jumps over the lazy dog')
        self.assertEqual(lower, 'the quick brown fox jumps over the lazy dog')

    def test_lower_some_caps(self):
        lower = lower_the_string('The Quick Brown Fox Jumps Over The Lazy Dog')
        self.assertEqual(lower, 'the quick brown fox jumps over the lazy dog')

    def test_lower_numbers(self):
        lower = lower_the_string('QWERTY 22 UIOP 33 ASDF 44 GHJKL 55')
        self.assertEqual(lower, 'qwerty 22 uiop 33 asdf 44 ghjkl 55')

    def test_lower_characters(self):
        lower = lower_the_string('QWERTY !@#$%^&*() UIOP []{} ASDF ;:<>/?')
        self.assertEqual(lower, 'qwerty !@#$%^&*() uiop []{} asdf ;:<>/?')


# Tests the slice_the_string function
class TestSliceString(unittest.TestCase):
    def test_letters(self):
        sliced = slice_the_string('qwertyuiopasdfghjkl')
        self.assertEqual(sliced, ' q w e r t y u i o p a s d f g h j k l ')

    def test_letters_numbers(self):
        sliced = slice_the_string('qwertyuiop12345')
        self.assertEqual(sliced, ' q w e r t y u i o p 1 2 3 4 5 ')

    def test_letters_numbers_characters(self):
        sliced = slice_the_string('qwerty12345!@#$%')
        self.assertEqual(sliced, ' q w e r t y 1 2 3 4 5 ! @ # $ % ')


# Tests the count_vowels function
class TestCountVowels(unittest.TestCase):
    def setUp(self):
        self.vowels = ('a', 'e', 'i', 'o', 'u', 'y')

    def test_count_all_letters(self):
        test_string = 'q u i c k f o x j u m p s o v e r l a z y d o g'
        count_letters = count_vowels(test_string, self.vowels)
        self.assertEqual(count_letters, [('a', 1), ('e', 1), ('i', 1), ('o', 3), ('u', 2), ('y', 1)])

    def test_count_letters_numbers(self):
        test_string = 'q u i c k f o x 2 3 4 5 j u m p s o v e r l a z y d o g'
        count_letters = count_vowels(test_string, self.vowels)
        self.assertEqual(count_letters, [('a', 1), ('e', 1), ('i', 1), ('o', 3), ('u', 2), ('y', 1)])

    def test_count_letters_characters(self):
        test_string = 'q u i c k ! @ # $ % j u m p s o v e r l a z y d o g'
        count_letters = count_vowels(test_string, self.vowels)
        self.assertEqual(count_letters, [('a', 1), ('e', 1), ('i', 1), ('o', 2), ('u', 2), ('y', 1)])

    def tearDown(self):
        self.vowels = None


# Tests the print_vowel_count function
class TestPrintCount(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_print_one_each(self):
        new_count = [('a', 1), ('e', 1), ('i', 1), ('o', 1), ('u', 1), ('y', 1)]
        print_vowel_count(new_count)
        self.assertEqual(sys.stdout.getvalue().strip(), "Vowel count for the string is:"
                                                        "\n\ta: 1"
                                                        "\n\te: 1"
                                                        "\n\ti: 1"
                                                        "\n\to: 1"
                                                        "\n\tu: 1"
                                                        "\n\ty: 1")


    def test_print_some(self):
        new_count = [('a', 2), ('e', 0), ('i', 2), ('o', 0), ('u', 2), ('y', 0)]
        print_vowel_count(new_count)
        self.assertEqual(sys.stdout.getvalue().strip(), "Vowel count for the string is:"
                                                        "\n\ta: 2"
                                                        "\n\ti: 2"
                                                        "\n\tu: 2")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
