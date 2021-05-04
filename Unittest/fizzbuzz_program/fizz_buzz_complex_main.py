"""
Author: Chris Caprio
Program: FizzBuzz
Details:
The program prints the numbers 1 to 100.
For multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.
"""

# Imports & Variables
from fizz_buzz_complex_functions import opening_info, enter_a_number, number_genterator
from fizz_buzz_complex_functions import print_list, count_print_fizzbuzz, play_again


# Function - this while loops runs/controls all of the functions
def start():
    playing = True
    while playing:
        first = 0

        print("\nEnter the Starting number")
        begin = enter_a_number(first)

        print("\nEnter the Ending number")
        end = enter_a_number(begin)

        fizzBuzz_list = number_genterator(begin, end)
        print_list(fizzBuzz_list)
        count_print_fizzbuzz(fizzBuzz_list)
        playing = play_again()


# Main - This while loop runs the start function
if __name__ == "__main__":
    while True:
        opening_info()
        start()
        break




