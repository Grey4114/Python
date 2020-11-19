"""
Program: FizzBuzz
Created: 11/18/2020
Updated:
Script Type: All In One Complexe FizzBuzz script
Project Source:
    Pierian Data's Complete Python 3 Bootcamp Projects List
    https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/18-Milestone%20Project%20-%203/02-Final%20Capstone%20Project%20Ideas.ipynb

Notes:
    In this adaptation of FizzBuzz the user is asked to enter number range (Ex. 85 to 123).
    The program will then list the number range, replacing multiples of 3 with Fizz, multiples of 5 with Buzz and
    multiples of 3 and 5 with FizzBuzz.
    The program will also keep a count of each type.

    This script is broken into two other scripts Main and Functions, to practice working with multiple scripts that
    are connected.
"""

from collections import Counter


""" --- Functions --- """
# Generate a list of numbers from start to end
def number_genterator():
    for num in range(start, end+1):
        if num % 3 == 0 and num % 5 == 0:
            number_list.append("FizzBuzz")
        elif num % 3 == 0:
            number_list.append("Fizz")
        elif num % 5 == 0:
            number_list.append("Buzz")
        else:
            number_list.append(num)

    return number_list


# Print the number list
def print_list(number_list):
    for x in number_list:
        print(f'\t{x}')


# Count the types and print the amounts
def count_print_fizzbuzz(number_list):
    fizzbuzz = Counter(number_list)
    print(f'\nCount of Fizzes & Buzzes'
          f'\n\tFizz: {fizzbuzz["Fizz"]}'
          f'\n\tBuzz: {fizzbuzz["Buzz"]}'
          f'\n\tFizzBuzz: {fizzbuzz["FizzBuzz"]}')


""" --- MAIN --- """
while True:
    print("\nWelcome to the FizzBuzz program")
    print("\t1) The program will ask you the user to enter number range (Ex. 85 to 123)")
    print("\t2) The program will print the number range")
    print("\t3) Numbers that are multiples of 3 are replaced with Fizz")
    print("\t4) Numbers that are multiples of 5 are replaced with Buzz")
    print("\t5) Numbers that are multiples of both 3 and 5 are replaced with FizzBuzz.")
    print("\t6) The program will also keep a count of each Fizz, Buzz and FizzBuzz.")
    input("Press Enter to continue")


    while True:
        start = 0
        end = 0
        number_list = []

        # Enter the starting number
        while True:
            try:
                start = int(input("\nEnter the starting number: "))
            except ValueError:
                print("Error! Enter a whole number!")
                continue
            break

        # Enter the ending number
        while True:
            try:
                end = int(input("Entet the ending number: "))
                if end <= start:
                    print("Error! End number must be higher then the starting number.")
                    continue
            except ValueError:
                print("Error! Enter a whole number!")
                continue
            break

        number_list = number_genterator()
        print_list(number_list)
        count_print_fizzbuzz(number_list)
        break
    break


