"""
Program: Change Return
Created: 11/17/2020
Script Type:  Unittest Script
Notes:
    This script tests change_return_functions.py script
"""

import sys
import unittest
from io import StringIO
from return_change_functions import choose_random_price, check_the_payment, calc_difference, calc_change, show_change


# Test the Random Price function
class TestRandomPrice(unittest.TestCase):
    def test_price(self):
        self.assertIn(choose_random_price(), (0.99, 1.94, 2.84, 3.59, 4.12))


# Test the Check The Payment function
class TestCheckPayment(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_payment_false(self):
        self.assertEqual(check_the_payment(4, 5), False)

    def test_payment_true(self):
        self.assertEqual(check_the_payment(5, 4), True)

    def test_payment_check_print(self):
        check_the_payment(5, 4)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Enter a dollar amount that is higher than the Purchase Price')

    def tearDown(self):
        self.payment_false = None
        self.payment_true = None


# Test the Calc Difference function
class TestCalcDifference(unittest.TestCase):
    def test_difference(self):
        self.assertEqual(calc_difference(4.12, 7), 2.88)


# Test the Calc Change function
class TestCalcChange(unittest.TestCase):
    def test_change_dollars(self):
        self.assertEqual(calc_change(3.00), (3, 0, 0, 0, 0))

    def test_change_quarters(self):
        self.assertEqual(calc_change(0.75), (0, 3, 0, 0, 0))

    def test_change_dimes(self):
        self.assertEqual(calc_change(0.20), (0, 0, 2, 0, 0))

    def test_change_nickel(self):
        self.assertEqual(calc_change(0.05), (0, 0, 0, 1, 0))

    def test_change_pennies(self):
        self.assertEqual(calc_change(0.03), (0, 0, 0, 0, 3))

    def test_change_one_of_each(self):
        self.assertEqual(calc_change(1.41), (1, 1, 1, 1, 1))

    def test_change_multiple(self):
        self.assertEqual(calc_change(3.94), (3, 3, 1, 1, 4))

    def test_change_negative_number(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calc_change(-3.94), (3, 3, 1, 1, 4))

    def test_change_no_number(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calc_change(None), (3, 3, 1, 1, 4))

    def test_change_text(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calc_change("number"), (3, 3, 1, 1, 4))


# Test the Show Change function
class TestShowChange(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_show_all_coins(self):
        show_change(1.93, (1, 3, 1, 1, 3))
        self.assertEqual(sys.stdout.getvalue().strip(), "The Return Change for $1.93 is:"
                                                        "\n\t1 Dollars"
                                                        "\n\t3 Quarters"
                                                        "\n\t1 Dimes"
                                                        "\n\t1 Nickels"
                                                        "\n\t3 Pennies")

    def test_show_some_coins(self):
        show_change(0.17, (0, 0, 1, 1, 2))
        self.assertEqual(sys.stdout.getvalue().strip(), "The Return Change for $0.17 is:"
                                                        "\n\t1 Dimes"
                                                        "\n\t1 Nickels"
                                                        "\n\t2 Pennies")


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
