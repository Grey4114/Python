"""
Author: Chris Caprio
Program: FizzBuzz
Program Detail:
The program prints the numbers 1 to 100.
For multiples of three print “Fizz” and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.

Notes:  This is a more robust version of the fizz_buzz_simple program.

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
    print("\t3) Multiples of 3 are replaced with Fizz")
    print("\t4) Multiples of 5 are replaced with Buzz")
    print("\t5) Multiples of both 3 and 5 are replaced with FizzBuzz.")
    print("\t6) A count of each Fizz, Buzz and FizzBuzz.")
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


