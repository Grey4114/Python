"""
Program: Fizz Buzz
Created: 11/18/2020
Updated:
Script Type: Complexe FizzBuzz script - Main Section only
Notes:
    In this adaptation of FizzBuzz the user is asked to enter number range (Ex. 85 to 123).
    The program will then list the number range, replacing multiples of 3 with Fizz, multiples of 5 with Buzz and
    multiples of 3 and 5 with FizzBuzz.
    The program will also keep a count of each type.
"""

from fizz_buzz_complex_functions import number_genterator, print_list, count_print_fizzbuzz


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

        number_list = number_genterator(start, end)
        print_list(number_list)
        count_print_fizzbuzz(number_list)
        break
    break
