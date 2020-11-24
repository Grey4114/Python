"""
Program: test_pig_latin_complex_class
Created: 11/23/2020
Script Type: Unittest script
Program Details:
    This script is designed to test the pig_latin_complex_class script

Notes:

"""

""" --- IMPORTS ---"""
import unittest
from pig_latin_complex_class import PigLatin



""" --- TEST CASES --- """
class TestPigLatin_Class(unittest.TestCase):
    def setUp(self):
        PigLatin()
        pass

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
