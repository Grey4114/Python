"""
Notes: Unittest script for the change_return_functions.py script
"""

# Imports
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from return_change_functions import opening_info, choose_random_price, enter_payment, calc_difference
from return_change_functions import calc_change, print_results, play_again
from return_change_main import prices


# TEST - test opening_info function
class TestOpeningInfo(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_opening_text(self):
        opening_info()
        self.assertEqual(sys.stdout.getvalue().strip(), "Welcome to the Change Return program."
                                                        "\n\t1) The player will be shown a Purchase Price"
                                                        "\n\t2) The Player will be asked to input a Payment amount."
                                                        "\n\t3) The return change will be shown.")

    def tearDown(self):
        pass


# TEST - test the choose_random_price function and prices variable
class TestRandomPrice(unittest.TestCase):
    def setUp(self):
        self.price = choose_random_price(prices)

    # Check the function
    def test_random_price(self):
        self.assertIn(self.price, (0.99, 1.94, 2.84, 3.59, 4.12))

    # Verify that prices are correct
    def test_prices(self):
        check = [0.99, 1.94, 2.84, 3.59, 4.12]
        for x in range(len(check)):
            self.assertEqual(prices[x], check[x])

    def tearDown(self):
        self.price = None


# TEST - Test the enter_payment function
class TestEnterPayment(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    # Price is 1.94 and input is 2, returns  2
    @patch('builtins.input', return_value=2)
    def test_higher_value(self, mock_input):
        pay = enter_payment(1.94)
        self.assertEqual(pay, 2)

    # todo - need to figure out how to test mock input with error text
    """
    # Price is 1.94 and input is 1, returns  error text
    @patch('builtins.input', return_value=1)
    def test_lower_value(self, mock_input):
        pay = enter_payment(1.94)
        self.assertEqual(sys.stdout.getvalue().strip(), "Enter a dollar amount that is higher than the Purchase Price")

    # Price is 1.94 and input no value, returns  error text
    @patch('builtins.input', return_value="")
    def test_no_value(self, mock_input):
        pay = enter_payment(1.94)
        self.assertEqual(sys.stdout.getvalue().strip(), "Enter a dollar amount that is higher than the Purchase Price")

    # Price is 1.94 and input text value, returns  error text
    @patch('builtins.input', return_value="a")
    def test_text_value(self, mock_input):
        pay = enter_payment(1.94)
        self.assertEqual(sys.stdout.getvalue().strip(), "Whoops! That's not a whole dollar amount. Please try again.")

    # Price is 1.94 and input negative value, returns  error text
    @patch('builtins.input', return_value=-1)
    def test_negative_value(self, mock_input):
        pay = enter_payment(1.94)
        self.assertEqual(sys.stdout.getvalue().strip(), "Enter a dollar amount that is higher than the Purchase Price")
    """

    def tearDown(self):
        pass


# TEST -  the calc_difference function
class TestCalcDifference(unittest.TestCase):
    def test_0_value(self):
        self.assertEqual(calc_difference(4.12, 0), -4.12)

    def test_lower_value(self):
        self.assertEqual(calc_difference(4.12, 3), -1.12)

    def test_higher_vaule(self):
        self.assertEqual(calc_difference(4.12, 5), 0.88)

    def test_veryhigh_vaule(self):
        self.assertEqual(calc_difference(4.12, 100), 95.88)


# TEST - the calc_change function
class TestCalcChange(unittest.TestCase):
    def test_change_dollars(self):
        self.assertEqual(calc_change(3.00), [3, 0, 0, 0, 0])

    def test_change_quarters(self):
        self.assertEqual(calc_change(0.75), [0, 3, 0, 0, 0])

    def test_change_dimes(self):
        self.assertEqual(calc_change(0.20), [0, 0, 2, 0, 0])

    def test_change_nickel(self):
        self.assertEqual(calc_change(0.05), [0, 0, 0, 1, 0])

    def test_change_pennies(self):
        self.assertEqual(calc_change(0.03), [0, 0, 0, 0, 3])

    def test_change_one_of_each(self):
        self.assertEqual(calc_change(1.41), [1, 1, 1, 1, 1])

    def test_change_multiple(self):
        self.assertEqual(calc_change(3.94), [3, 3, 1, 1, 4])

    def test_change_no_number(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calc_change(None), [3, 3, 1, 1, 4])

    def test_change_text(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calc_change("number"), [3, 3, 1, 1, 4])


# TEST - the print_results function
class TestSPrintResults(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    # Diff is 1.93 and gives at least one of each coin return
    def test_show_all_coins(self):
        print_results(1.93, (1, 3, 1, 1, 3))
        self.assertEqual(sys.stdout.getvalue().strip(), "The Return Change is $1.93:"
                                                        "\n1 : Dollars"
                                                        "\n3 : Quarters"
                                                        "\n1 : Dimes"
                                                        "\n1 : Nickels"
                                                        "\n3 : Pennies")

    # Diff is 1.11 and show some coins, not all
    def test_show_some_coins(self):
        print_results(1.11, (1, 0, 1, 0, 1))
        self.assertEqual(sys.stdout.getvalue().strip(), "The Return Change is $1.11:"
                                                        "\n1 : Dollars"
                                                        "\n1 : Dimes"         
                                                        "\n1 : Pennies")

    # Diff is 0, does not show any coins
    def test_no_coins(self):
        print_results(0.0, (0, 0, 0, 0, 0))
        self.assertEqual(sys.stdout.getvalue().strip(), "The Return Change is $0.0:")


    def tearDown(self):
        pass


# TEST - the play_again function
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
