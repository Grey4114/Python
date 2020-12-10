"""
Author: Chris Caprio
Program: Quiz Maker
Details:
Make an application which takes randomly picked questions from a csv file and puts together a quiz for students.
Each quiz can be different and then reads a key to grade the quizzes.

Notes: Program scores 10 point for each correct answer and gives a total at end.

"""


" --- VARIABLES --- "
import random
import csv



" --- FUNCTIONS --- "
# Opens the questions.csv file and drops the info into a list
def get_text_from_csv_file():
    q_data = open('questions.csv', 'r')   # Open the csv file using read
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


# Prints the answer list
def print_answers(count, answers):
    return f"\t{count}) {answers}"

# Prints the answer list
def print_score(points):
    return f'\n\tTotal Score: {points}'



" --- MAIN --- "
def main(questions, q_num_list, ques_count, points):
    while True:
        # For loop prints the question
        for x in q_num_list:
            correct_answer = 0
            answ_count = 0
            ques_count += 1
            print(print_question(ques_count, questions[x][0]))
            a_num_list = answers_number_list()

            # For loop prints the list of answers
            for y in a_num_list:
                answ_count += 1
                print(print_answers(answ_count, questions[x][y]))
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


    return points

if __name__ == "__main__":
    playing = True

    # Main loop
    while playing:
        # Setup the variables
        questions = get_text_from_csv_file()
        q_num_list = question_number_list()
        ques_count = 0
        points = 0

        # Print the greeting
        print_greeting()

        # Run the main program and print the score
        points = main(questions, q_num_list, ques_count, points)
        print(print_score(points))


        # START - Play again loop
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



