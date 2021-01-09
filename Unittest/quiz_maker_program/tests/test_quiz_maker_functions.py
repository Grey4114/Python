"""
Author: Chris Caprio
Program: Quiz Maker
Notes: Unittest tests of the quiz_maker_functions.py script
"""

" --- IMPORTS --- "
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from quiz_maker_functions import get_text_from_csv_file, generate_random_number
from quiz_maker_functions import question_number_list, answers_number_list
from quiz_maker_functions import print_score, prints_answers, print_question, print_greeting
from quiz_maker_functions import correct_answer, select_answer, check_choice_answer, play_again


" --- TEST CASES --- "
# Test that the fucntion gets the text from the CSV file
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

# Test that random numbers are being generated within the specified range
class TestGenerateNumber(unittest.TestCase):
    def test_question_range(self):
        start = 1
        end = 45
        for x in range(0, end):
            num = generate_random_number(start, end)
            self.assertIsNot(num, num < start, num > end)

    def test_answer_range(self):
        start = 1
        end = 3
        for x in range(0, end):
            num = generate_random_number(start, end)
            # print(num)
            self.assertIsNot(num, num < start, num > end)

# Test that there are no duplicate numbers and that 10 numbers are generated
class TestQuestionNumberList(unittest.TestCase):
    def setUp(self):
        self.questionNumbers = question_number_list()

    def test_number_list_size(self):
        num = self.questionNumbers
        self.assertEqual(len(num), 10)

    def test_numbers_in_range(self):
        num = self.questionNumbers
        for x in num:
            self.assertIsNot(x, x < 1, x > 44)

    def tearDown(self):
        self.questionNumbers = None

# Test that there are no duplicate numbers and that 3 numbers are generated
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

# Check that the Greeting text is being printed when the function is called
class TestGreeting(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.greeting = print_greeting()


    def test_greeting_text(self):
        self.greeting
        self.assertEqual(sys.stdout.getvalue().strip(), "Welcome to the Quiz Maker program"
                                                        "\n\tThere are 10 questions and each correct answer is worth 10 points."
                                                        "\n\tAnswer all 10 questions and see how well you do."
                                                        "\n\tGood Luck!!")

    def tearDown(self):
        self.greeting = None
        

# Test that the questions are being shown correctly
class TestPrintQuestion(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        count = 1
        question = 'The plural of MOOSE is?'
        self.quest_info = print_question(count, question)

    def test_question_text(self):
        print(self.quest_info)
        self.assertEqual(sys.stdout.getvalue().strip(), "Question 1: The plural of MOOSE is?")

    def tearDown(self):
        self.quest_info = None

# Test that the points text is being shown correctly
class TestPrintScore(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        points = 60
        self.score = print_score(points)

    def test_score_text(self):
        print(self.score)
        self.assertEqual(sys.stdout.getvalue().strip(), "Total Score: 60")

    def tearDown(self):
        self.score = None

# Test that the answer list text is being shown correctly
class TestPrintAnswer(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        a_num_list = (1, 2, 3)
        answ_count = 0
        questions = ('The plural of MOOSE is?', 'Moose', 'Meese', 'Maus')
        self.answers = prints_answers(a_num_list, answ_count, questions)

    def test_answer_text(self):
        self.answers
        self.assertEqual(sys.stdout.getvalue().strip(), "1) Moose"
                                                        "\n\t2) Meese"
                                                        "\n\t3) Maus")

    def tearDown(self):
        self.answers = None

# Tests the position of the correct answer
class TestCorrectAnswer(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        a_num_list = (3, 2, 1)
        self.correct_answer = correct_answer(a_num_list)

    def test_answer_number(self):
        self.assertEqual(self.correct_answer, 3)

    def tearDown(self):
        self.correct_answer = None

# Tests user input for the answer number
class TestSelectAnswer(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    @patch('builtins.input', return_value=1)
    def test_number_1(self, mock_input):
        answer = select_answer()
        self.assertEqual(answer, 1)

    @patch('builtins.input', return_value=2)
    def test_number_2(self, mock_input):
        answer = select_answer()
        self.assertEqual(answer, 2)

    @patch('builtins.input', return_value=3)
    def test_number_3(self, mock_input):
        answer = select_answer()
        self.assertEqual(answer, 3)

    # TODO - Unabel to get the mock input to work correctly for the 3 test cases, skipping for now
    """
    choice = [4, 1]
    # Todo - raise error test invalid number
    @patch('builtins.input', side_effect=[2,choice])
    def test_input_number_outside_range(self, mock_input):
        for x in range(mock_input):
            select_answer()
            with self.assertRaises(ValueError):
                self.assertEqual(sys.stdout.getvalue().strip(), 'Value Error! 1, 2 or 3')

    # Todo - raise error test nothing entered
    @patch('builtins.input', return_value=4)
    def test_input_a_space(self, mock_input):
        with self.assertRaises(ValueError):
                self.assertEqual(select_answer(), 'Value Error! Enter 1, 2 or 3')


    # Todo - raise error test letter entered
    @patch('builtins.input', return_value='a')
    def test_input_a_letter(self, mock_input, mock_input2):
        with self.assertRaises(ValueError):
                self.assertEqual(select_answer(), 'Value Error! Enter 1, 2 or 3')
    """

    def tearDown(self):
        pass

# Tests the compare choice to correct answer, response and points increase
class TestCheckChoiceAnswer(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.points = 20
        self.choice = 3
        self.correct_answer_number = 3
        self.incorrect_answer_number = 1

    def test_incorrect_answer(self):
        check_choice_answer(self.points, self.choice, self.incorrect_answer_number)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Incorrect')

    def test_incorrect_points(self):
        incorrect = check_choice_answer(self.points, self.choice, self.incorrect_answer_number)
        self.assertEqual(incorrect, 20)

    def test_correct_answer(self):
        check_choice_answer(self.points, self.choice, self.correct_answer_number)
        self.assertEqual(sys.stdout.getvalue().strip(), 'Correct')

    def test_correct_points(self):
        correct = check_choice_answer(self.points, self.choice, self.correct_answer_number)
        self.assertEqual(correct, 30)

    def tearDown(self):
        self.points = None
        self.choice = None
        self.correct_answer_number = None
        self.incorrect_answer_number = None


# Tests user input for play again function
class TestPlayAgain(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    @patch('builtins.input', return_value='y')
    def test_input_yes(self, mock_input):
        play = play_again()
        self.assertEqual(play, True)

    @patch('builtins.input', return_value='n')
    def test_input_no(self, mock_input):
        play = play_again()
        self.assertEqual(play, False)

    @patch('builtins.input', return_value='n')
    def test_input_no_text_check(self, mock_input):
        play = play_again()
        self.assertEqual(sys.stdout.getvalue().strip(), "Thanks for playing!!")


    # TODO - Unabel to get the mock input to work correctly for the 3 test cases, skipping for now
    """
    @patch('builtins.input', return_value='z')
    def test_input_letter(self, mock_input):
        play = play_again()
        self.assertEqual(sys.stdout.getvalue().strip(), "Please enter 'Y' or 'N'.")

    @patch('builtins.input', return_value='')
    def test_input_space(self, mock_input):
        play = play_again()
        self.assertEqual(play, True)

    @patch('builtins.input', return_value=5)
    def test_input_number(self, mock_input):
        play = play_again()
        self.assertEqual(play, True)
    """

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
