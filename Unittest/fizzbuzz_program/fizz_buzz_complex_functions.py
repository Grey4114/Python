"""
Author: Chris Caprio
Program: FizzBuzz - functions
"""

# Froms, Imports & Variables
from collections import Counter


# Function - Applications opening/start up info
def opening_info():
    print("\nWelcome to the FizzBuzz program")
    print("\tThe user can enter number range (Ex. 85 to 123) and number range will be shown")
    print("\t- Multiples of 3 are replaced with Fizz")
    print("\t- Multiples of 5 are replaced with Buzz")
    print("\t- Multiples of 3 and 5 are replaced with FizzBuzz")


# Function - User enters a number
def enter_a_number(first):
    num = 0
    while True:
        try:
            num = int(input("Number: "))
            if num <= first:
                print("Error! Enter a higher number.")
                continue
        except ValueError:
            print("Error! Enter a whole number!")
            continue
        break
    return num


# Function - Generates the list of numbers with Fizz, Buzz and FizzBuzz
def number_genterator(begin, end):
    return ["FizzBuzz" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else num for num in range(begin, end+1)]


# Function - Print the number list
def print_list(fizzBuzz_list):
    print("\nFizzBuzz List")
    print(*[f'\t{x}' for x in fizzBuzz_list], sep="\n")


# Function - Count the types and print the amounts
def count_print_fizzbuzz(fizzBuzz_list):
    count = Counter(fizzBuzz_list)
    print(f'\n----------\n\tFizz: {count["Fizz"]}\n\tBuzz: {count["Buzz"]}\n\tFizzBuzz: {count["FizzBuzz"]}')


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



