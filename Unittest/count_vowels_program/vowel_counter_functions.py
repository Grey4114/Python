"""
Author: Chris Caprio
Program: Count Vowels
Notes: Functions section of the vowel_counter.py script
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



