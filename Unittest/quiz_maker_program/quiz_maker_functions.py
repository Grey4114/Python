"""
Author: Chris Caprio
Program: Quiz Maker
Notes: This is the Functions section of the original quiz_maker.py script
"""


" --- VARIABLES --- "
import random
import csv

" --- FUNCTIONS --- "
# Opens the questions.csv file and drops the info into a list
def get_text_from_csv_file():
    q_data = open('D:\\GitHub\\Python\\Unittest\\quiz_maker_program\\questions.csv', 'r')   # Open the csv file using read
    csv_data = csv.reader(q_data)    # Read all of the lines of info
    q_lines = list(csv_data)
    q_data.close()    # Close the file
    return q_lines


# Generates a random number
def generate_random_number(start, end):
    return random.randint(start, end)


# Calls for 10 random numbers and checks to make sure there are no duplicates
def question_number_list():
    questionNumberList = []
    while len(questionNumberList) < 10:
        n = generate_random_number(1, 44)
        if n not in questionNumberList:
            questionNumberList.append(n)
    return questionNumberList


# Calls for 3 random numbers and checks to make sure there are no duplicates
def answers_number_list():
    count = 0
    answerNumberList = []
    while count < 3:
        x = generate_random_number(1, 3)
        if x not in answerNumberList:
            count += 1
            answerNumberList.append(x)
    return answerNumberList


# Prints the question
def print_greeting():
    print("\nWelcome to the Quiz Maker program")
    print("\tThere are 10 questions and each correct answer is worth 10 points.")
    print("\tAnswer all 10 questions and see how well you do.")
    print("\tGood Luck!!")


# Prints the question
def print_question(count, question):
    return f"\nQuestion {count}: {question}"


# Prints the total points scored
def print_score(points):
    return f'\n\tTotal Score: {points}'


# Print the list of answer choices
def prints_answers(a_num_list, answ_count, questions):
    for y in a_num_list:
        answ_count += 1
        print(f"\t{answ_count}) {questions[y]}")


# Finds the position of the correct answer
def correct_answer(a_num_list):
        return a_num_list.index(1) + 1


# Player inputs the answer number and returns it
def select_answer():
    while True:
        try:
            choice = int(input("Answer: "))
            if choice < 1 or choice > 3:
                raise ValueError()
        except ValueError:
            print('\tValue Error! Enter 1, 2 or 3')
            continue
        break
    return choice


# Compare choice to correct answer, give response and apply points
def check_choice_answer(points, choice, correct_answer_number):
    if choice == correct_answer_number:
        print(f'\tCorrect')
        points = points + 10
    else:
        print(f'\tIncorrect')

    return points


# Play again loop
def play_again():
    playing = True
    while True:
        play_again = input("\nPlay Again (Y,N): ")
        if play_again.upper() == "Y":
            break
        elif play_again.upper() == "N":
            print(f"\nThanks for playing!!")
            playing = False
            break
        else:
            print("Please enter 'Y' or 'N'.")
    return playing


