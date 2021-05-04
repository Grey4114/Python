"""
Author: Chris Caprio
Program: FizzBuzz
Notes: Unittest test script for testing the fizz_buzz_complex_functions.py script
"""

# Imports & Variables
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from fizz_buzz_complex_functions import opening_info, enter_a_number, number_genterator
from fizz_buzz_complex_functions import print_list, count_print_fizzbuzz, play_again


# TEST - check that the opening text has not changed and is being shown
class TestOpeningInfo(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_opening_text(self):
        opening_info()
        self.assertEqual(sys.stdout.getvalue().strip(), "Welcome to the FizzBuzz program"
                                                        "\n\tThe user can enter number range (Ex. 85 to 123) and number range will be shown"
                                                        "\n\t- Multiples of 3 are replaced with Fizz"
                                                        "\n\t- Multiples of 5 are replaced with Buzz"
                                                        "\n\t- Multiples of 3 and 5 are replaced with FizzBuzz")

    def tearDown(self):
        self.open = None


# TEST - check that the input is a positive number
class TestEnterNumber(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    # todo - get mock to work with error text
    """
    # Input nothing, returns an error
    @patch('builtins.input', return_value='')
    def test_input_none(self, mock_input):
        number = enter_a_number(0)
        self.assertEqual(sys.stdout.getvalue().strip(), "Error! Enter a whole number!")

    # Input a space, returns an error
    @patch('builtins.input', return_value=' ')
    def test_input_space(self, mock_input):
        number = enter_a_number(0)
        self.assertEqual(sys.stdout.getvalue().strip(), "Error! Enter a whole number!")

    # Input a letter, returns an error
    @patch('builtins.input', return_value='w')
    def test_input_letter(self, mock_input):
        number = enter_a_number(0)
        self.assertEqual(sys.stdout.getvalue().strip(), "Error! Enter a whole number!")

    # Input a special character, returns an error
    @patch('builtins.input', return_value='$')
    def test_input_special(self, mock_input):
        number = enter_a_number(0)
        self.assertEqual(sys.stdout.getvalue().strip(), "Error! Enter a whole number!")

    # Input a negative number, returns an error
    @patch('builtins.input', return_value=-2)
    def test_input_negativeNumber(self, mock_input):
        number = enter_a_number(0)
        self.assertEqual(sys.stdout.getvalue().strip(), "Error! Enter a whole number!")
    """

    def tearDown(self):
        pass


# TEST - check that the beginning input number is a positive number
class TestEnterNumber_Begin(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    # todo - get mock to work with error text
    """
    # Input 0, returns an error
    @patch('builtins.input', return_value=0)
    def test_inputBegin_0(self, mock_input):
        number = enter_a_number(0)
        self.assertEqual(sys.stdout.getvalue().strip(), "Error! Enter a higher number.")
    """

    # Input a number, returns the number
    @patch('builtins.input', return_value=7)
    def test_inputBegin_singleDigit(self, mock_input):
        number = enter_a_number(0)
        self.assertEqual(number, 7)

    # Input a multiple digit number, returns the number
    @patch('builtins.input', return_value=53)
    def test_inputBegin_multipleDigits(self, mock_input):
        number = enter_a_number(0)
        self.assertEqual(number, 53)


# TEST - check that the ending input number is a positive number and greater then the starting number
class TestEnterNumber_End(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    # todo - get mock to work with error text
    """
    # Input same number as begin, returns an error
    @patch('builtins.input', return_value=1)
    def test_inputEnd_sameAsBegin(self, mock_input):
        number = enter_a_number(1)
        self.assertEqual(sys.stdout.getvalue().strip(), "Error! Enter a higher number.")


    # Input a number that is lower then the beginning number, returns an error
    @patch('builtins.input', return_value=1)
    def test_inputEnd_lessThenBegin(self, mock_input):
        number = enter_a_number(2)
        self.assertEqual(sys.stdout.getvalue().strip(), "Error! Enter a higher number.")
    """

    # Input a number greater then the beginnin number, returns the number
    @patch('builtins.input', return_value=5)
    def test_inputEnd_greaterThenBegin(self, mock_input):
        number = enter_a_number(1)
        self.assertEqual(number, 5)

    def tearDown(self):
        pass


# TEST - check the number generator producing Fizz, Buzz and FizzBuzz
class TestNumberGenerator(unittest.TestCase):
    def test_gen_noFizzBuzz(self):
        number = number_genterator(1, 2)
        self.assertEqual(number, [1, 2])

    def test_gen_oneFizz(self):
        number = number_genterator(1, 3)
        self.assertEqual(number, [1, 2, 'Fizz'])

    def test_gen_oneBuzz(self):
        number = number_genterator(4, 5)
        self.assertEqual(number, [4, 'Buzz'])

    def test_gen_oneFizzBuzz(self):
        number = number_genterator(28, 30)
        self.assertEqual(number, [28, 29, 'FizzBuzz'])

    def test_gen_allThree(self):
        number = number_genterator(10, 15)
        self.assertEqual(number, ['Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'])


# TEST - checks that the printed info is correct
class TestPrintList(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_print_noFizzBuzzes(self):
        print_list([1, 2])
        self.assertEqual(sys.stdout.getvalue().strip(), "FizzBuzz List"
                                                        "\n\t1"
                                                        "\n\t2")

    def test_print_oneFizz(self):
        print_list([1, 2, 'Fizz'])
        self.assertEqual(sys.stdout.getvalue().strip(), "FizzBuzz List"
                                                        "\n\t1"
                                                        "\n\t2"
                                                        "\n\tFizz")

    def test_print_oneBuzz(self):
        print_list([4, 'Buzz'])
        self.assertEqual(sys.stdout.getvalue().strip(), "FizzBuzz List"
                                                        "\n\t4"
                                                        "\n\tBuzz")

    def test_print_oneFizzBuzz(self):
        print_list([28, 29, 'FizzBuzz'])
        self.assertEqual(sys.stdout.getvalue().strip(), "FizzBuzz List"
                                                        "\n\t28"
                                                        "\n\t29"
                                                        "\n\tFizzBuzz")

    def test_print_allThree(self):
        print_list(['Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'])
        self.assertEqual(sys.stdout.getvalue().strip(), "FizzBuzz List"
                                                        "\n\tBuzz"
                                                        "\n\t11"
                                                        "\n\tFizz"
                                                        "\n\t13"
                                                        "\n\t14"
                                                        "\n\tFizzBuzz")

    def tearDown(self):
        pass


# TEST - counts the number of Fizz, Buzz and FizzBuzz, then checks the totals and printed totals
class TestCountFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_count_noFizzBuzzes(self):
        count_print_fizzbuzz([1, 2])
        self.assertEqual(sys.stdout.getvalue().strip(), "----------"
                                                        "\n\tFizz: 0"
                                                        "\n\tBuzz: 0"
                                                        "\n\tFizzBuzz: 0")

    def test_count_oneFizz(self):
        count_print_fizzbuzz([1, 2, 'Fizz'])
        self.assertEqual(sys.stdout.getvalue().strip(), "----------"
                                                        "\n\tFizz: 1"
                                                        "\n\tBuzz: 0"
                                                        "\n\tFizzBuzz: 0")

    def test_count_oneBuzz(self):
        count_print_fizzbuzz([4, 'Buzz'])
        self.assertEqual(sys.stdout.getvalue().strip(), "----------"
                                                        "\n\tFizz: 0"
                                                        "\n\tBuzz: 1"
                                                        "\n\tFizzBuzz: 0")

    def test_count_oneFizzBuzz(self):
        count_print_fizzbuzz([28, 29, 'FizzBuzz'])
        self.assertEqual(sys.stdout.getvalue().strip(), "----------"
                                                        "\n\tFizz: 0"
                                                        "\n\tBuzz: 0"
                                                        "\n\tFizzBuzz: 1")

    def test_count_allThree(self):
        count_print_fizzbuzz(['Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'])
        self.assertEqual(sys.stdout.getvalue().strip(), "----------"
                                                        "\n\tFizz: 1"
                                                        "\n\tBuzz: 1"
                                                        "\n\tFizzBuzz: 1")

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
