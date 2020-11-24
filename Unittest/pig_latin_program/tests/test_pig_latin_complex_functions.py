"""
Program: test_pig_latin_complex_functions
Created: 11/23/2020
Script Type: Unittest script
Program Details:
    This script is designed to test the pig_latin_complex_functions script

Notes:

"""

""" --- IMPORTS --- """
import unittest
from pig_latin_complex_functions import transform_word, check_word_type, convert_sentance
from pig_latin_complex_functions import print_pig_latin_word, print_pig_latin_sentance


""" --- TEST CASES --- """
class TestTransformWord(unittest.TestCase):
    def setUp(self):
        transform_word()
        pass

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        pass


class TestCheckWordType(unittest.TestCase):
    def setUp(self):
        check_word_type()
        pass

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        pass


class TestConvertSentance(unittest.TestCase):
    def setUp(self):
        convert_sentance()
        pass

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        pass


class TestPrintPigLatinWord(unittest.TestCase):
    def setUp(self):
        print_pig_latin_word()
        pass

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        pass


class TestPrintPigLatinSentance(unittest.TestCase):
    def setUp(self):
        print_pig_latin_sentance()
        pass

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        pass




if __name__ == '__main__':
    unittest.main()
