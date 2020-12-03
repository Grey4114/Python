"""
Author: Chris Caprio
Program: FizzBuzz
Details:
The program prints the numbers 1 to 100.
For multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.

Notes: Main section of the fizz_buzz_complex.py script

"""

from fizz_buzz_complex_functions import number_genterator, print_list, count_print_fizzbuzz


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
