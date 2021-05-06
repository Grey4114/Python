"""
Author: Chris Caprio
Program: Quiz Maker
Notes: Unittest tests of the quiz_maker_functions.py script
"""

# Import and Variables
import os
import os.path
import csv
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from quiz_maker_functions import opening_info, get_text_from_csv_file, question_number_list
from quiz_maker_functions import answers_number_list, print_question, choice_list, input_answer
from quiz_maker_functions import add_points, print_answers, print_score, play_again



# TEST - check that the opening text has not changed and is being shown
class TestOpeningInfo(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_opening_text(self):
        opening_info()
        self.assertEqual(sys.stdout.getvalue().strip(), "Welcome to the Quiz Maker program"
                                                        "\n\tThere are 10 random questions."
                                                        "\n\tEach correct answer is worth 10 points."
                                                        "\n\tGood Luck!")

    def tearDown(self):
        pass


# TEST - Test that the fucntion gets the text from the CSV file
class TestGetTextCSVFile(unittest.TestCase):
    def setUp(self):
        self.csvText = get_text_from_csv_file()

    # Note- The first line of the CSV file is one, there is no line 0
    def test_csv_line1_heading(self):
        heading_text = self.csvText
        self.assertEqual(heading_text[0], ['QUESTION', ' Correct Anaswer', ' Incorrect Answer 1', ' Incorrect Answer 2'])

    def test_csv_line20_question(self):
        line_text = self.csvText
        self.assertEqual(line_text[19][0], 'What is the main character in a story called?')

    def test_csv_line20_answer1(self):
        line_text = self.csvText
        self.assertEqual(line_text[19][1], ' Protagonist')

    def test_csv_line20_answer2(self):
        line_text = self.csvText
        self.assertEqual(line_text[19][2], ' Narrator')

    def test_csv_line20_answer3(self):
        line_text = self.csvText
        self.assertEqual(line_text[19][3], ' Antagonist')

    def test_csv_text_verify_45_lines(self):
        lines_of_text = self.csvText
        self.assertEqual(len(lines_of_text), 45)

    def tearDown(self):
        self.csvText = None


# TEST - Test that there are no duplicate numbers and that 10 numbers are generated
class TestQuestionNumberList(unittest.TestCase):
    def setUp(self):
        os.chdir("D:/GitHub/Python/Unittest/quiz_maker_program")
        self.held, sys.stdout = sys.stdout, StringIO()
        questions = get_text_from_csv_file()
        self.questionNumbers = question_number_list(questions)

    def test_number_list_size(self):
        num = self.questionNumbers
        self.assertEqual(len(num), 10)

    def test_numbers_in_range(self):
        num = self.questionNumbers
        for x in num:
            self.assertIsNot(x, x < 1, x > 44)

    def tearDown(self):
        self.questionNumbers = None


# TEST - Test that there are no duplicate numbers and that 3 numbers are generated
class TestAnswerNumberList(unittest.TestCase):
    def setUp(self):
        self.answerNumbers = answers_number_list()

    def test_list_size(self):
        num = self.answerNumbers
        self.assertEqual(len(num), 3)

    def test_numbers_in_range(self):
        num = self.answerNumbers
        for x in num:
            self.assertIsNot(x, x < 1, x > 3)

    def tearDown(self):
        self.answerNumbers = None


# TEST - Test that the questions are being shown correctly
class TestPrintQuestion(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        count = 1
        question = 'The plural of MOOSE is?'
        self.quest_info = print_question(count, question)

    def test_question_text(self):
        self.quest_info
        self.assertEqual(sys.stdout.getvalue().strip(), "Question 1: The plural of MOOSE is?")

    def tearDown(self):
        self.quest_info = None


# TEST - Test that the 3 answers are shown in a list
class TestChoiceList(unittest.TestCase):
    def setUp(self):
        os.chdir("D:/GitHub/Python/Unittest/quiz_maker_program")
        self.held, sys.stdout = sys.stdout, StringIO()
        self.questions = get_text_from_csv_file()
        self.a_num_list = (3, 1, 2)

    def test_question_15_list(self):
        choice_list(15, self.a_num_list, self.questions)
        self.assertEqual(sys.stdout.getvalue().strip(), "1)  Noun\n\t2)  Both\n\t3)  Adjective")

    def tearDown(self):
        self.questions = None
        self.a_num_list = None


# TEST - Tests the input answer number
class TestInputAnswer(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    # Inputs 1 and returns the number 1
    @patch('builtins.input', return_value=1)
    def test_valid_number_1(self, mock_input):
        num = input_answer()
        self.assertEquals(num, 1)

    # Inputs 2 and returns the number 2
    @patch('builtins.input', return_value=2)
    def test_valid_number_2(self, mock_input):
        num = input_answer()
        self.assertEquals(num, 2)

    # Inputs 3 and returns the number 3
    @patch('builtins.input', return_value=3)
    def test_valid_number_3(self, mock_input):
        num = input_answer()
        self.assertEquals(num, 3)

    # todo - get mock to work with error text
    """
    # Inputs 0 and returns error
    @patch('builtins.input', return_value=0)
    def test_invalid_number_0(self, mock_input):
        num = input_answer()
        self.assertEqual(sys.stdout.getvalue().strip(), '\tError! Enter 1, 2 or 3')

    # Inputs 'a' and returns a value error
    @patch('builtins.input', return_value='a')
    def test_invlaid_letter(self, mock_input):
        flips = input_flips()
        self.assertEqual(sys.stdout.getvalue().strip(), '\tError! Enter 1, 2 or 3')

    # Inputs '' and returns a value error
    @patch('builtins.input', return_value='')
    def test_invalid_space(self, mock_input):
        input_flips()
        self.assertEqual(sys.stdout.getvalue().strip(), '\tError! Enter 1, 2 or 3')
    """

    def tearDown(self):
        pass


# TEST - Test that getting a correct answer adds 10 points to the point counter
# and that the correct or incorrect text is printed
class TestAddPoints(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_correct_text_points(self):
        num = add_points(10, 2, 2)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Correct')
        self.assertEqual(num, 20)

    def test_incorrect_text_points(self):
        num = add_points(10, 1, 2)
        self.assertEqual(num, 10)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Incorrect')

    def tearDown(self):
        pass


# TEST - Test that each answer in the answer list is printed correctly
class TestPrintAnswers(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_answer_1(self):
        print_answers(1, "Moon")
        self.assertEqual(sys.stdout.getvalue().strip(), "1) Moon")

    def test_answer_2(self):
        print_answers(2, "Jungle")
        self.assertEqual(sys.stdout.getvalue().strip(), "2) Jungle")

    def test_answer_3(self):
        print_answers(3, "Time")
        self.assertEqual(sys.stdout.getvalue().strip(), "3) Time")

    def tearDown(self):
        pass


# TEST - Test that the points text is being shown correctly
class TestPrintScore(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_score_text(self):
        print_score(60)
        self.assertEqual(sys.stdout.getvalue().strip(), "Total Score: 60")

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
