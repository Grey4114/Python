"""
Author: Chris Caprio
Program: FizzBuzz
Notes: Unittest test script for testing the fizz_buzz_complex_functions.py script
"""


import sys
import unittest
from io import StringIO
from fizz_buzz_complex_functions import number_genterator, print_list, count_print_fizzbuzz



class TestNumberGenerator(unittest.TestCase):
    def test_number_list(self):
        number = number_genterator(23, 30)
        self.assertEqual(number, [23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz'])


class TestPrintList(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        number_list = [23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz']
        self.num_list = print_list(number_list)


    def test_print_the_list(self):
        self.num_list
        self.assertEqual(sys.stdout.getvalue().strip(), "23"
                                                        "\n\tFizz"
                                                        "\n\tBuzz"
                                                        "\n\t26"
                                                        "\n\tFizz"
                                                        "\n\t28"
                                                        "\n\t29"
                                                        "\n\tFizzBuzz")

    def tearDown(self):
        self.num_list = None


class TestCountPrintFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        number_list = [23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz']
        self.count = count_print_fizzbuzz(number_list)

    def test_something(self):
        self.count
        self.assertEqual(sys.stdout.getvalue().strip(), "Count of Fizzes & Buzzes"
                                                        "\n\tFizz: 2"
                                                        "\n\tBuzz: 1"
                                                        "\n\tFizzBuzz: 1")

    def tearDown(self):
        self.count = None


if __name__ == '__main__':
    unittest.main()
