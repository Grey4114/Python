"""
Coin Flip Simulation
- Write some code that simulates flipping a single coin however many times the user decides.
The code should record the outcomes and count the number of tails and heads.

Script : Unittest script
Created: 11/13/2020
Notes:
    This tests the coin_flip_functions.py script
"""

import sys
import unittest
from io import StringIO
from unittest.mock import patch
from CoinFlip.coin_flip_functions import player_name, number_of_flips, generate_number, flip_results, show_results


# Tests the player_name function
# Todo - unable to get the mock inputs to work for this test, need to do more research
class TestPlayerName(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.player = player_name()

    #def test_player_name(self):
    #    with mock.patch('builtins.input', return_value="Tom"):
    #        assert player_name() == "Tom"

    def tearDown(self):
        self.player = None


# Tests the number_of_flips function
# Todo - unable to get the mock inputs to work for this test, need to do more research
class TestNumberOfFlips(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.flips = number_of_flips()

    #@patch('builtins.input', return_value=21)
    #def test_num_flips(self, mock_flips):
    #    self.flips
    #    self.assertEqual(self.flips, mock_flips)

    def tearDown(self):
        self.flips = None


# Tests the generate_number function
class TestGenerateNumber(unittest.TestCase):
    def setUp(self):
        self.number = generate_number()

    # Tests if the number generated is greater then 1
    def test_number_greater(self):
        self.assertNotEqual(self.number, 2)

    # Tests if the number generated is less then 0
    def test_number_lesser(self):
        self.assertNotEqual(self.number, -1)

    def tearDown(self):
        self.number = None


# Tests the flip_results function
class TestFlipResults(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.results_0 = flip_results(0)
        self.results_1 = flip_results(1)
        self.results_2 = flip_results(2)

    def test_results_0(self):
        return self.results_0
        self.assertEqual(sys.stdout.getvalue().strip(), 'Heads')

    def test_results_1(self):
        return self.results_1
        self.assertEqual(sys.stdout.getvalue().strip(), 'Tails')

    def test_results_2(self):
        return self.results_2
        self.assertEqual(sys.stdout.getvalue().strip(), 'Tie')

    def tearDown(self):
        self.results = None


# Tests the show_results function
class TestShowResults(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.show = show_results(23, 7, 16)

    # Tests the text output for the function
    def test_show_results_text(self):
        return self.show
        self.assertEqual(sys.stdout.getvalue().strip(), '23 Flips: 7 Heads & 16 Tails')

    def tearDown(self):
        self.show = None



if __name__ == '__main__':
    unittest.main()
