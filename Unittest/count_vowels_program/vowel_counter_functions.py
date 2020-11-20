"""
Program: Count Vowels
Created: 11/19/2020
Updated:
Script Type: Functions Only
Project Source:
    Pierian Data's Complete Python 3 Bootcamp Projects List
    https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/18-Milestone%20Project%20-%203/02-Final%20Capstone%20Project%20Ideas.ipynb

Program Details:
    Enter a string and the program counts the number of vowels in the text.
    For added complexity have it report a sum of each vowel found.

Notes:
    The vowel_counter script was split into the 2 scripts, vowel_counter_main and vowel_counter_functions
    to test working with mutiple connected script.
"""

""" --- VARIABLES --- """
# vowels = ('a', 'e', 'i', 'o', 'u', 'y')



""" --- FUNCTIONS --- """
# Function - Make the string lower case
def lower_the_string(start_string):
    new_string = start_string.lower()
    return new_string


# Function - slice up the string
def slice_the_string(new_string):
    slice_string = new_string.replace('', ' ')
    return slice_string


# Function - count the vowels
def count_vowels(slice_string, vowels):
    vowel_count = []
    for let in vowels:
        count = 0
        for char in slice_string:
            if let == char:
                count += 1

        vowel_count.append((let, count))
    return vowel_count


# Function - Print the vowel count
def print_vowel_count(vowel_count):
    print('Vowel count for the string is:')

    for x in range(len(vowel_count)):
        if vowel_count[x][1] > 0:
            print(f'\t{vowel_count[x][0]}: {vowel_count[x][1]}')



