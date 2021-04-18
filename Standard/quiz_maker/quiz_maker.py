"""
Author: Chris Caprio
Program: Quiz Maker
Details:
Make an application which takes randomly picked questions from a csv file and puts together a quiz for students.
Each quiz can be different and then reads a key to grade the quizzes.
"""

# From, Imports and Variables
import random
import csv


# Prints the question
def start_info():
    print("\nWelcome to the Quiz Maker program")
    print("\tThere are 10 random questions, each worth 10 points.")
    input('Press ENTER to continue ')


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


# Finction - Prints the question
def print_question(count, question):
    print(f"\nQuestion {count}: {question}")


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


# Main - This area runs all of the functions
if __name__ == "__main__":
    playing = True

    while playing:
        # Setup counters
        ques_count = 0
        points = 0

        # Print the greeting
        start_info()
        
        # Setup the numbers & questions variables
        questions = get_text_from_csv_file()
        num_list = question_number_list(questions)

        # Main loop prints questions, answers and score
        while True:
            # For loop prints the question
            for x in num_list:
                correct_answer = 0
                answ_count = 0
                ques_count += 1
                print_question(ques_count, questions[x][0])
                a_num_list = answers_number_list()

                # For loop prints the list of answers
                for y in a_num_list:
                    answ_count += 1
                    print_answers(answ_count, questions[x][y])
                    correct_answer = a_num_list.index(1) + 1

                # Player inputs the answer number
                while True:
                    try:
                        choice = int(input("Answer: "))
                        if choice < 1 or choice > 3:
                            raise ValueError('\tError! Enter 1, 2 or 3')
                    except ValueError as e:
                        print(e)
                        continue
                    break

                # Compare choice to correct answer, give response and apply points
                if choice == correct_answer:
                    points += 10
                    print(f'\tCorrect')
                else:
                    print(f'\tIncorrect')
            break

        # Prints points and play again
        print(print_score(points))
        playing = play_again()

