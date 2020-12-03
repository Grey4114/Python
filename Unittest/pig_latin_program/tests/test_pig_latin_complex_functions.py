"""
Author: Chris Caprio
Program: Pig Latin
Notes: Unittest script that tests the pig_latin_complex_functions.py script

"""

""" --- IMPORTS --- """
import sys
from io import StringIO
import unittest
from pig_latin_complex_functions import transform_word, check_for_vowel, convert_sentance, user_choice
from pig_latin_complex_functions import print_pig_latin_word, print_pig_latin_sentance


""" --- TEST CASES --- """
class TestCheckForVowel(unittest.TestCase):
    def test_single_letter_vowel(self):
        test_word = check_for_vowel('a')
        self.assertEqual(test_word, 0)

    def test_single_vowel(self):
        test_word = check_for_vowel('ire')
        self.assertEqual(test_word, 0)

    def test_two_vowel(self):
        test_word = check_for_vowel('yeti')
        self.assertEqual(test_word, 0)

    def test_one_consonant(self):
        test_word = check_for_vowel('made')
        self.assertEqual(test_word, 1)

    def test_two_consonants(self):
        test_word = check_for_vowel('trick')
        self.assertEqual(test_word, 2)

    def test_three_consonants(self):
        test_word = check_for_vowel('strunge')
        self.assertEqual(test_word, 3)


class TestTransformWord(unittest.TestCase):
    def test_single_letter_vowel(self):
        test_word = transform_word('a')
        self.assertEqual(test_word, 'away')

    def test_single_vowel(self):
        test_word = transform_word('ire')
        self.assertEqual(test_word, 'ireway')

    def test_two_vowel(self):
        test_word = transform_word('yeti')
        self.assertEqual(test_word, 'yetiway')

    def test_one_consonant(self):
        test_word = transform_word('made')
        self.assertEqual(test_word, 'ademay')

    def test_two_consonants(self):
        test_word = transform_word('trick')
        self.assertEqual(test_word, 'icktray')

    def test_three_consonants(self):
        test_word = transform_word('strunge')
        self.assertEqual(test_word, 'ungestray')


class TestConvertSentance(unittest.TestCase):
    def test_vowel_string_caps(self):
        sentance = convert_sentance("I AM OSCAR")
        self.assertEqual(sentance, "iway amway oscarway")

    def test_consonant_string_caps(self):
        sentance = convert_sentance("QUICK BROWN STRANGE FOX")
        self.assertEqual(sentance, "uickqay ownbray angestray oxfay")

    def test_mix_string(self):
        sentance = convert_sentance("The Yeti Screamed Frightfully Into The Night")
        self.assertEqual(sentance, "ethay yetiway eamedscray ightfullyfray intoway ethay ightnay")


class TestUserChoice_Words(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()


    def test_word_single_vowel(self):
        user_choice('w', 'a', "")
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Word: a\n\tPig Latin Word: away")


    def test_word_vowel(self):
        user_choice('w', 'yeti', "")
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Word: yeti\n\tPig Latin Word: yetiway")


    def test_word_one_consonant(self):
        user_choice('w', 'sure', "")
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Word: sure\n\tPig Latin Word: uresay")


    def test_word_two_consonant(self):
        user_choice('w', 'trick', "")
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Word: trick\n\tPig Latin Word: icktray")


    def test_word_three_consonant(self):
        user_choice('w', 'string', "")
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Word: string\n\tPig Latin Word: ingstray")


    def tearDown(self):
        pass


class TestUserChoice_Sentance(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()


    def test_sentance_single_word_vowel(self):
        user_choice('s', '', 'yeti')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Sentance: yeti"
                                                        "\n\tPig Latin Sentance: yetiway")

    def test_sentance_single_word_consonant(self):
        user_choice('s', '', 'teach')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Sentance: teach"
                                                        "\n\tPig Latin Sentance: eachtay")

    def test_sentance_vowels(self):
        user_choice('s', '', 'i am oscar')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Sentance: i am oscar"
                                                        "\n\tPig Latin Sentance: iway amway oscarway")

    def test_sentance_consonant(self):
        user_choice('s', '', 'quick brown strang fox')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Sentance: quick brown strang fox"
                                                        "\n\tPig Latin Sentance: uickqay ownbray angstray oxfay")

    def test_sentance_mix(self):
        user_choice('s', '', 'the yeti screamed frightfully into the night')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Sentance: the yeti screamed frightfully into the night"
                                                        "\n\tPig Latin Sentance: ethay yetiway eamedscray ightfullyfray intoway ethay ightnay")

    def tearDown(self):
        pass


class TestPrintPigLatinWord(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()


    def test_word_single_vowel(self):
        print_pig_latin_word('a', 'away')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Word: a\n\tPig Latin Word: away")


    def test_word_vowel(self):
        print_pig_latin_word('yeti', 'yetiway')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Word: yeti\n\tPig Latin Word: yetiway")


    def test_word_one_consonant(self):
        print_pig_latin_word('sure', 'uresay')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Word: sure\n\tPig Latin Word: uresay")


    def test_word_two_consonant(self):
        print_pig_latin_word('trick', 'icktray')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Word: trick\n\tPig Latin Word: icktray")


    def test_word_three_consonant(self):
        print_pig_latin_word('string', 'ingstray')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Word: string\n\tPig Latin Word: ingstray")


    def tearDown(self):
        pass


class TestPrintPigLatinSentance(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()


    def test_sentance_vowel_string(self):
        print_pig_latin_sentance('i am oscar', 'iway amway oscarway')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Sentance: i am oscar"
                                                        "\n\tPig Latin Sentance: iway amway oscarway")

    def test_sentance_consonant(self):
        print_pig_latin_sentance('quick brown strang fox', 'uickqay ownbray angstray oxfay')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Sentance: quick brown strang fox"
                                                        "\n\tPig Latin Sentance: uickqay ownbray angstray oxfay")

    def test_sentance_mix(self):
        print_pig_latin_sentance('the yeti screamed frightfully into the night', 'ethay yetiway eamedscray ightfullyfray intoway ethay ightnay')
        self.assertEqual(sys.stdout.getvalue().strip(), "Oringal Sentance: the yeti screamed frightfully into the night"
                                                        "\n\tPig Latin Sentance: ethay yetiway eamedscray ightfullyfray intoway ethay ightnay")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
