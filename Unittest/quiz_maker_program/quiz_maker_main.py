"""
Author: Chris Caprio
Program: Quiz Maker
Details:
Make an application which takes randomly picked questions from a csv file and puts together a quiz for students.
Each quiz can be different and then reads a key to grade the quizzes.
Program scores 10 point for each correct answer and gives a total at end.
"""
# Import and Variables
from quiz_maker_functions import opening_info, get_text_from_csv_file, question_number_list, answers_number_list
from quiz_maker_functions import choice_list, input_answer, add_points, print_question, print_score, play_again



# Function -  Main loop prints questions, answers and score
def start(points, ques_count, questions):
    while True:
        # For loop prints the question
        for x in num_list:
            correct_answer = 0
            # answ_count = 0
            ques_count += 1
            print_question(ques_count, questions[x][0])
            a_num_list = answers_number_list()

            # Prints the list of choices
            choice_list(x, a_num_list, questions)

            # Note which answer is the correct one
            correct_answer = a_num_list.index(1) + 1

            # Player inputs the answer number
            choice = input_answer()

            # Compare choice to correct answer, give response and apply points
            points = add_points(points, choice, correct_answer)
        break
    return points


# Main - This loop does the program setup and runs the start function
if __name__ == "__main__":
    playing = True
    while playing:
        # Setup counters
        ques_count = 0
        points = 0

        # Print the greeting
        opening_info()

        # Setup the numbers & questions variables
        questions = get_text_from_csv_file()
        num_list = question_number_list(questions)

        # Main loop prints questions, answers and score
        points = start(points, ques_count, questions)

        # Prints points and play again
        print_score(points)
        playing = play_again()
