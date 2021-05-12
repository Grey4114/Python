"""
Author: Chris Caprio
Program: Quiz Maker - functions
"""

# From, Imports and Variables
import random
import csv


# Function - Prints the question
def opening_info():
    print("\nWelcome to the Quiz Maker program")
    print("\tThere are 10 random questions.")
    print("\tEach correct answer is worth 10 points.")
    print("\tGood Luck!")


# Function - Opens the questions.csv file and drops the info into a list
def get_text_from_csv_file():
    q_data = open('questions.csv', 'r')       # Open the csv file using read
    q_lines = list(csv.reader(q_data))        # Read all of the lines into a list
    q_data.close()                            # Close the file
    return q_lines


# Function - Generates 10 random numbers from questions list
def question_number_list(questions):
    numList = list(range(1, len(questions)))
    random.shuffle(numList)
    return numList[0:10]


# Function - Randomize the numbers 1,2,3
def answers_number_list():
    ansList = [1, 2, 3]
    random.shuffle(ansList)
    return ansList


# Function - Prints the question
def print_question(count, question):
    print(f"\nQuestion {count}: {question}")


# Function - prints the list of answers
def choice_list(x, a_num_list, questions):
    answ_count = 0
    for y in a_num_list:
        answ_count += 1
        print_answers(answ_count, questions[x][y])


# Function - Player inputs the answer number
def input_answer():
    while True:
        try:
            choice = int(input("Choice: "))
            if choice < 1 or choice > 3:
                raise ValueError('\tError! Enter 1, 2 or 3')
        except ValueError:
            print('\tError! Enter a valid number')
            continue
        break
    return choice


# Function - Compare choice to correct answer, give response and apply points
def add_points(points, choice, correct_answer):
    if choice == correct_answer:
        points += 10
        print(f'\tCorrect')
    else:
        print(f'\tIncorrect')

    return points


# Function - Prints the answer list
def print_answers(count, answers):
    print(f"\t{count}) {answers}")


# Function - Prints the answer list
def print_score(points):
    print(f'\n\tTotal Score: {points}')


# Function - Asks the player to play again - Player Input
def play_again():
    while True:
        play_again = input("\nPlay Again (Y,N): ")
        if play_again.upper() == "Y":
            return True
        elif play_again.upper() == "N":
            print("\nThanks for playing!!")
            return False
        else:
            print("Please enter 'Y' or 'N'.")

