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
from io import StringIO
import unittest
from CoinFlip.coin_flip_functions import player_name, number_of_flips, generate_number, flip_results, show_results


class TestPlayerName(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.card = Card('Hearts', 'Ace')

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        self.card = None


class TestNumberOfFlips(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.card = Card('Hearts', 'Ace')

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        self.card = None


class TestGenerateNumber(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.card = Card('Hearts', 'Ace')

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        self.card = None


class TestFlipResults(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.card = Card('Hearts', 'Ace')

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        self.card = None


class TestShowResults(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.card = Card('Hearts', 'Ace')

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        self.card = None



if __name__ == '__main__':
    unittest.main()
