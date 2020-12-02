"""
Program: Quiz Maker
Created: 12/1/2020 -
Script Type:
    One script - contains variables, functions, classes and main

Project Source:
    Pierian Data's Complete Python 3 Bootcamp Projects List
    https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/18-Milestone%20Project%20-%203/02-Final%20Capstone%20Project%20Ideas.ipynb

Program Details:
    Make an application which takes various questions form a file, picked randomly, and puts together a quiz for
    students. Each quiz can be different and then reads a key to grade the quizzes.

Notes:

"""


""" --- VARIABLES --- """
# OS functions - how to see and access all files in a directory
# import os
import random

question_Areas = ['History', 'Literature', 'Geography', 'Sciences', 'Mathematics']
question_StartEnd = ((2, 11), (14, 23), (26, 35), (38, 47), (50, 59))
numberSets = []



""" --- CLASSES --- """





""" --- FUNCTIONS --- """
def get_random_numbers():
    for number_pair in question_StartEnd:
        start = number_pair[0]
        end = number_pair[1]
        new_set = []
        count = 0

        while count < 3:
            num = random.randint(start, end)
            if num not in new_set:
                count += 1
                new_set.append(num)
        numberSets.append(new_set)
    return numberSets




def get_text_from_file():
    question = open('questions.txt', 'r')   # Open the text file using read
    line = question.readlines()     # Read all of the lines of text
    question.close()    # Close the file
    return line


def print_question(count, line):
    return f"Q{count}: {line}"


def print_answers():
    pass



def question_answer():
    line = get_text_from_file()
    numberSets = get_random_numbers()
    count = 0

    # for loop - read and print each line
    for numSet in numberSets:
        ac = 0
        area = question_Areas
        print(area[ac])
        ac += 1
        for x in numSet:
            count += 1
            print(print_question(count, line[x - 1]))


question_answer()





""" --- MAIN --- """










