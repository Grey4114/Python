"""
Author: Chris Caprio
Program: Coin Flip Simulation
Notes: Unittest script for testing the coin_flip_function.py script
"""

# Imports
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from coin_flip_functions import input_flips, flip_the_coin, show_results, play_again


# TESTS - Tests the input number of flips
class TestInputFlips(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    # Inputs 5 and returns the number 5
    @patch('builtins.input', return_value=5)
    def test_input_valid_number(self, mock_input):
        flips = input_flips()
        self.assertEquals(flips, 5)

    # Inputs 0 and returns the number 0
    @patch('builtins.input', return_value=0)
    def test_input_valid_0(self, mock_input):
        flips = input_flips()
        self.assertEquals(flips, 0)


    # todo - get mock to work with error text
    """
    # Inputs 'a' and returns a value error
    @patch('builtins.input', return_value='a')
    def test_input_invlaid_letter(self, mock_input):
        flips = input_flips()
        self.assertEqual(sys.stdout.getvalue().strip(), "Error! That's not a number. Please try again.")

    # Inputs '' and returns a value error
    @patch('builtins.input', return_value='')
    def test_input_invalid_space(self, mock_input):
        input_flips()
        self.assertEqual(sys.stdout.getvalue().strip(), "Error! That's not a number. Please try again.")
    """

    def tearDown(self):
        pass


# TESTS - the flip_the_coin function
class TestFlipTheCoin(unittest.TestCase):
    # Inputs 0 flips and returns 0
    def test_0_flips(self):
        self.assertEqual(len(flip_the_coin(0)), 0)

    # Inputs 7 flips and returns 7
    def test_7_flips(self):
        self.assertEqual(len(flip_the_coin(7)), 7)

    # Inputs 22 flips and returns 22
    def test_22_flips(self):
        self.assertEqual(len(flip_the_coin(22)), 22)

    # Inputs 123 flips and returns 123
    def test_123_flips(self):
        self.assertEqual(len(flip_the_coin(123)), 123)

    # Inputs a negative -5 flips and returns 0
    def test_negative_number_flips(self):
        self.assertEqual(len(flip_the_coin(-5)), 0)


# TEST - the show_results function
class TestShowResults(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    # User input 0 flips
    def test_0_flips_results(self):
        show_results([])
        self.assertEqual(sys.stdout.getvalue().strip(), '0 Flips: 0 Heads & 0 Tails')

    # User input 1 flip and it was heads
    def test_1_heads_results(self):
        show_results([0])
        self.assertEqual(sys.stdout.getvalue().strip(), 'Heads\n1 Flips: 1 Heads & 0 Tails')

    # User input 1 flip and it was tails
    def test_1_tails_results(self):
        show_results([1])
        self.assertEqual(sys.stdout.getvalue().strip(), 'Tails\n1 Flips: 0 Heads & 1 Tails')

    # User input 4 flips - 2 heads, 2 tails
    def test_2heads_2tails_results(self):
        show_results([0,1,0,1])
        self.assertEqual(sys.stdout.getvalue().strip(), 'Heads\nTails\nHeads\nTails\n4 Flips: 2 Heads & 2 Tails')

    def tearDown(self):
        pass



# Tests the play_again function
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


if __name__ == '__main__':
    unittest.main()
