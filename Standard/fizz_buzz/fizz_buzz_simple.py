"""
Author: Chris Caprio
Program: FizzBuzz
Program Detail:
The program prints the numbers 1 to 100.
For multiples of three print “Fizz” and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.

Notes:  This is a very simple first pass of the program

"""

# Function - Applications opening/start up info
def start_info():
    print("\nFizzBuzz program")
    print("\t- Prints a list of number from 1 - 100 ")
    print("\t- Multiples of 3 are replaced with Fizz")
    print("\t- Multiples of 5 are replaced with Buzz")
    print("\t- Multiples of both 3 and 5 are replaced with FizzBuzz")


# Function - Prints the list of number with Fizz, Buzz and FizzBuzz
def number_genterator():
    return [print("\tFizzBuzz") if num % 3 == 0 and num % 5 == 0 else print("\tFizz") if num % 3 == 0 else print("\tBuzz") if num % 5 == 0 else print("\t", num) for num in range(1, 101) ]


# Main - This area runs all of the functions
if __name__ == "__main__":
    start_info()
    number_genterator()




