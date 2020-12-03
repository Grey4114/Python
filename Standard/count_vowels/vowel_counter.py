"""
Author: Chris Caprio
Program: Count Vowels
Details: Enter a string and the program counts the number of vowels in the text. For added complexity have it report
a sum of each vowel found.

"""

""" --- VARIABLES --- """
vowels = ('a', 'e', 'i', 'o', 'u', 'y')



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



""" --- MAIN --- """
# Main > Intro & Rules > Enter string > Check string > count vowels > show results > play again
# Starting/Main loop
while True:
    print('\nWelcome to the Vowel Counter program')
    print('\tHow the program works:')
    print('\tEnter a string of words or letters')
    print('\tThe program will count the vowels and return the count for each vowel.')
    input('Press Enter to continue')

    # Input string loop
    while True:
        try:
            start_string = input('\nEnter in a word, sentence or string: ')
            if not start_string:
                raise ValueError('\tError! Empty string, please try again')
        except ValueError as e:
            print(e)
            continue

        # Exits string loop
        break

    new_string = lower_the_string(start_string)   
    slice_string = slice_the_string(new_string)
    vowel_count = count_vowels(slice_string, vowels)
    print_vowel_count(vowel_count)

    # Exit Main loop
    break

