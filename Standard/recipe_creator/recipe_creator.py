"""
Author: Chris Caprio
Program: Recipe Maker
Details:
Create a recipe class with ingredients and a put them in a recipe manager program that organizes them into
categories like deserts, main courses or by ingredients like chicken, beef, soups, pies etc.

Notes:
    Import / export info to/from CSV files
"""

" --- IMPORTS --- "
import csv

" --- VARIABLES --- "
recipes_file = "D:\\GitHub\\Python\\Standard\\recipe_creator\\recipes.csv"
ingrediants_file = "D:\\GitHub\\Python\\Standard\\recipe_creator\\ingrediants.csv"

recipe_type = ('Main Meal', 'Candy', 'Cookie', 'Cake', 'Pie', 'Soup', 'Sandwich', 'Salad')
ingrediant_type = ('Spice', 'Fruit', 'Vegitable', 'Condiment', 'Protien', 'Grains')

main_dict = {1: 'Recipe', 2: 'Ingrediants', 3: 'Exit'}
menu_dict = {1: 'View All', 2: 'Find By Type', 3: 'Add', 4: 'Main Menu'}


" --- CLASSES --- "
# Recipe class
class Recipes:
    def __init__(self, recipe_type, recipes_file, main_dict, menu_dict):
        self.recipes_file = recipes_file
        self.recipe_type = recipe_type
        self.main_dict = main_dict
        self.menu_dict = menu_dict

    # Opens the CSV file and drops the info into a list
    def read_recipes_file(self):
        recipe_file = open(self.recipes_file, 'r')
        csv_reader = csv.reader(recipe_file)
        recipe_data = list(csv_reader)
        recipe_file.close()
        return recipe_data

    # Opens the CSV file and writes a new line to it
    def write_recipes_file(self, recipe_info):
        recipe_file = open(self.recipes_file, 'a', newline='')
        recipe_writer = csv.writer(recipe_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        recipe_writer.writerow(recipe_info)
        recipe_file.close()

    # Prints a full list of all recipes
    def list_recipes_all(self, recipe_data):
        print(f'\nAll Recipes')
        print(f'--------------')
        count = 1
        for x in range(1, len(recipe_data)):
            print(f'\t{count}) {recipe_data[x][1]} - {recipe_data[x][0]}')
            count += 1
        return len(recipe_data)

    # Prints a list of recipes by type
    def list_recipes_type(self, res_type, recipe_data):
        menu_list = []
        print(f'\n{res_type} Recipes')
        print(f'--------------')
        count = 1
        for x in range(1, len(recipe_data)):
            if recipe_data[x][0] == res_type:
                print(f'\t{count}) {recipe_data[x][1]}')
                count += 1
                menu_list.append(recipe_data.index(recipe_data[x]))

        return len(recipe_data), menu_list

    # Prints one full recipe and its ingrediants
    def list_full_recipe(self, res_num, recipe_data):
        print(f'\n{recipe_data[res_num][1]} Recipe')
        print(f'-------------------------')
        for x in range(2, len(recipe_data[res_num])):
            print(f'\t{recipe_data[res_num][x]}')


# Ingrediants class
class Ingrediants:
    def __init__(self, ingrediant_type, ingrediants_file, main_dict, menu_dict):
        self.ingrediant_type = ingrediant_type
        self.ingrediants_file = ingrediants_file
        self.main_dict = main_dict
        self.menu_dict = menu_dict

    # Opens the CSV file and drops the info into a list
    def read_ingrediants_file(self):
        ingre_file = open(self.ingrediants_file, 'r')
        csv_reader = csv.reader(ingre_file)
        ingrediant_data = list(csv_reader)
        ingre_file.close()
        return ingrediant_data

    # Opens the CSV file and writes a new line to it
    def write_ingrediants_file(self, ingrediants_info):
        ingrediant_file = open(ingrediants_file, 'a', newline='')
        ingrediant_writer = csv.writer(ingrediant_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ingrediant_writer.writerow(ingrediants_info)
        ingrediant_file.close()


    # Prints a full list of all recipes
    def list_ingrediants_all(self, ingrediant_data):
        print(f'\nAll Ingrediants')
        print(f'--------------')
        count = 1
        for x in range(1, len(ingrediant_data)):
            print(f'\t{count}) {ingrediant_data[x][1]} - {ingrediant_data[x][0]}')
            count += 1
        return len(ingrediant_data)

    # Prints a list of recipes by type
    def list_ingrediants_type(self, ingre_type, ingrediant_data):
        print(f'\n{ingre_type} Ingrediants')
        print(f'------------------------')
        count = 1
        for x in range(1, len(ingrediant_data)):
            if ingrediant_data[x][0] == ingre_type:
                print(f'\t{count}) {ingrediant_data[x][1]}')
                count += 1
        return len(ingrediant_data)


" --- FUNCTIONS --- "
# This prints the startup info for the program
def welcome():
    print("\nWelcome to the Recipe Manager")
    print("\tView and add ingrediants and recipes.")
    input("\tPress any key to continue ")


# The main menu function
def main_menu(main_dict):
    print("\nMain Menu")
    print("------------")
    for x in range(0, len(main_dict)):
        print(f"\t{x+1}) {main_dict[x+1]}")
    return len(menu_dict)


# For Loop that prints out the menu
def general_menu(main_dict, menu_dict):
    print(f"\n{main_dict} Menu")
    print("------------------")
    for x in range(0, len(menu_dict)):
        print(f"\t{x+1}) {menu_dict[x+1]}")
    return len(menu_dict)


# While loop - input choice for the general_menu function
def menu_choice(length):
    selection = -1
    while True:
        try:
            selection = int(input("\tSelect an Option: "))
            if selection < 0 or selection > length:
                raise ValueError()
        except ValueError:
            print('\tValue Error! Enter a valid number')
            continue
        break
    return selection


# Sets variables for either recipe or ingrediant types
def choice_RI_type(choice_type, recipe_data, ingrediant_data, recipe_type, ingrediant_type):
    if choice_type == 1:
        data = recipe_data
        info_type = recipe_type
    else:
        data = ingrediant_data
        info_type = ingrediant_type
    return data, info_type


# Lists either the recipe or ingrediants by choice_type
def type_list(info_type, choice_type, main_dict):
    print(f'\nSelect a {main_dict[choice_type]} Type')
    for x in range(0, len(info_type)):
        print(f'\t{x}) {info_type[x]}')
    return len(info_type)


# Add a recipe or ingrediant to the respective csv file
def add_data(info_type, choice_type, main_dict, data, recipes, ingrediants):
    add_info = []
    print(f'\n\nAdd {main_dict[choice_type]}')
    add_loop = True

    while True:
        type_list(info_type, choice_type, main_dict)
        type_choice = int(input('Choice: '))
        add_info.append(info_type[type_choice])
        name = input(f'\nEnter a {info_type[type_choice]} {main_dict[choice_type]} name: ')
        add_info.append(name)

        if choice_type == 1:
            count = 2
            while add_loop:
                ingred = ingrediants.read_ingrediants_file()
                ingrediants.list_ingrediants_all(ingred)
                add_ingred = int(input('\nSelect an ingrediant: '))
                add_info.append(ingred[add_ingred][1])
                print(f'- {ingred[add_ingred][1]} Added')

                while True:
                    yes_no = input(f'\nAdd another ingrediant (y/n): ')
                    if yes_no.lower() != 'n' and yes_no.lower() != 'y':
                        print('Incorrect Entry! Try again.')
                    elif yes_no.lower() == 'n':
                        add_loop = False
                        break
                    else:
                        break

            recipes.write_recipes_file(add_info)
            print(f'\nNew {main_dict[choice_type]} - {add_info[1]} ({add_info[0]})')
            print(f'Ingrediants - ', end="")
            for x in add_info[2:]:
                print(f'{x}, ', end="")

            print("")

        else:
            ingrediants.write_ingrediants_file(add_info)
            print(f'New {main_dict[choice_type]} - {add_info[1]} ({add_info[0]})')
        break



" --- MAIN FUNCTION --- "
def main():
    recipes = Recipes(recipe_type, recipes_file, main_dict, menu_dict)
    ingrediants = Ingrediants(ingrediant_type, ingrediants_file, main_dict, menu_dict)

    while True:
        looping = True
        choice_type = 0
        choice = 0
        length = 0
        num_selected = 0

        recipe_data = recipes.read_recipes_file()
        ingrediant_data = ingrediants.read_ingrediants_file()

        length = main_menu(main_dict)
        choice_type = menu_choice(length)

        # Exit option from main menu
        if choice_type == 3:
            break

        # Main Loop
        while looping:
            data, info_type = choice_RI_type(choice_type, recipes, ingrediants, recipe_type, ingrediant_type)
            length = general_menu(main_dict[choice_type], menu_dict)
            choice = menu_choice(length)

            # Prints either the full recipe or ingrediants list
            if choice == 1:
                if choice_type == 1:
                    length = recipes.list_recipes_all(recipe_data)
                    res_num = menu_choice(length)
                    recipes.list_full_recipe(res_num, recipe_data)
                    input('\nPress any key to return to the Main Menu ')
                    looping = False

                else:
                    ingrediants.list_ingrediants_all(ingrediant_data)
                    input('\nPress any key to return to the Main Menu ')
                    looping = False

            # Prints either a list of recipes or ingrediants by type
            elif choice == 2:
                if choice_type == 1:
                    type_length = type_list(info_type, choice_type, main_dict)
                    sel_type = menu_choice(type_length)
                    type_length, menu_list = recipes.list_recipes_type(info_type[sel_type], recipe_data)

                    if len(menu_list) > 0:
                        num_selected = menu_choice(type_length)
                        res_num = menu_list[num_selected-1]
                        recipes.list_full_recipe(res_num, recipe_data)
                    else:
                        print('\tNo recipes of this type available')

                    input('\nPress any key to return to the Main Menu ')
                    looping = False

                else:
                    type_length = type_list(info_type, choice_type, main_dict)
                    sel_type = menu_choice(type_length)
                    ingrediants.list_ingrediants_type(info_type[sel_type], ingrediant_data)

                    input('\nPress any key to return to the Main Menu ')
                    looping = False

            # Adds eithe a recipe or an ingrediant to the respective csv file
            elif choice == 3:
                add_data(info_type, choice_type, main_dict, data, recipes, ingrediants)
                input('\nPress any key to return to the Main Menu ')
                looping = False
            else:
                break


" --- NAME SPACE --- "
if __name__ == "__main__":
    welcome()
    main()
    print('\nThanks for playing!')


