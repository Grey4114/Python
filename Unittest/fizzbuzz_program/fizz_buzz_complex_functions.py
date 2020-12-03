"""
Author: Chris Caprio
Program: FizzBuzz
Notes: Functions section of the fizz_buzz_complex.py script
"""

from collections import Counter


""" --- Functions --- """
# Generate a list of numbers from start to end
def number_genterator(start, end):
    number_list = []
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

num = number_genterator(23, 30)
print(num)


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

