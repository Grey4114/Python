"""
Author: Chris Caprio
Program: FizzBuzz
Program Detail:
The program prints the numbers 1 to 100.
For multiples of three print “Fizz” and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.

Notes:  This is a very simple first pass of the program

"""


def number_genterator():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)






