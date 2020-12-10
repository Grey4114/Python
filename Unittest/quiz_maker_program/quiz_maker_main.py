"""
Author: Chris Caprio
Program: Quiz Maker
Details:
Make an application which takes randomly picked questions from a csv file and puts together a quiz for students.
Each quiz can be different and then reads a key to grade the quizzes.
Program scores 10 point for each correct answer and gives a total at end.

Notes: This is the Main section of the original quiz_maker.py script

"""


" --- IMPORTS --- "
from quiz_maker_functions import get_text_from_csv_file, question_number_list, answers_number_list
from quiz_maker_functions import print_score, print_greeting, print_question, prints_answers
from quiz_maker_functions import correct_answer, select_answer, check_choice_answer, play_again


" --- MAIN --- "
def main(questions, q_num_list, ques_count):
    # Print the greeting
    print_greeting()
    points = 0

    while True:
        # For loop prints the question
        for x in q_num_list:
            # Setup variables
            correct_answer_number = 0
            answ_count = 0
            ques_count += 1

            # Runs the function and prints the question
            print(print_question(ques_count, questions[x][0]))

            # Runs the function that generates a randon list of the answer numbers
            a_num_list = answers_number_list()

            # Runs the function and prints the list of answers
            prints_answers(a_num_list, answ_count, questions[x])

            # Runs the function that finds the position of the correct answer and returns it
            correct_answer_number = correct_answer(a_num_list)

            # Runs the function, user can enter choice and that number is returned
            choice = select_answer()

            # Runs the function, checks choice against answer, returns points and prints result
            points = check_choice_answer(points, choice, correct_answer_number)

        break
    print(print_score(points))


if __name__ == "__main__":
    playing = True

    # Main loop
    while playing:
        # Setup the variables
        questions = get_text_from_csv_file()
        q_num_list = question_number_list()
        ques_count = 0

        # Run the main function
        main(questions, q_num_list, ques_count)

        # Run the play again function
        playing = play_again(playing)



