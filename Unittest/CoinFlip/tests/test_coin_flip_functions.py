"""
Program: Coin Flip Simulation
Script : Unittest script
Created: 11/13/2020
Updated: 11/17/2020
Notes:
    This tests the coin_flip_functions.py script
"""

import sys
import unittest
from io import StringIO
from coin_flip_functions import generate_number, flip_results, flip_the_coin, show_results


""" --- TEST CASES --- """
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

    # Checks that 0 prints Heads
    def test_results_0(self):
        flip_results(0)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Heads')

    # Checks that 1 prints Tails
    def test_results_1(self):
        flip_results(1)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Tails')

    def tearDown(self):
        pass


# Tests the flip_the_coin function
class TestFlipCoin(unittest.TestCase):

    def test_flip_coin(self):
        self.assertEqual(len(flip_the_coin(7)), 7)


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
