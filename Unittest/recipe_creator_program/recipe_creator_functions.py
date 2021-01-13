"""
Author: Chris Caprio
Program: Recipe Creator
Notes: This is the Functions section of the original recipe_creator_main.py script
"""
" --- IMPORTS --- "
from recipe_creator_classes import recipes_file, recipe_type, ingrediant_type, ingrediants_file, main_dict, menu_dict
from recipe_creator_classes import Recipes, Ingrediants


" --- FUNCTIONS --- "
# This prints the startup info for the program
def welcome():
    print("\nWelcome to the Recipe Manager")
    print("\tView and add ingrediants and recipes.")


# The main menu function
def main_menu(main_dict):
    print("\nMain Menu")
    print("------------")
    for x in range(0, len(main_dict)):
        print(f"\t{x+1}) {main_dict[x+1]}")
    return len(main_dict)


# For Loop that prints out the menu
def general_menu(main_dict, menu_dict):
    print(f"\n{main_dict} Menu")
    print("------------------")
    for x in range(0, len(menu_dict)):
        print(f"\t{x+1}) {menu_dict[x+1]}")
    return len(menu_dict)


# While loop - input choice for the general_menu function
def menu_choice(length):
    selection = 0
    while True:
        try:
            selection = int(input("\tSelect an Option: "))
            if selection < 1 or selection > length:
                raise ValueError()
        except ValueError:
            print('\tValue Error! Enter a valid number')
            continue
        break
    return selection


# Sets variables for either recipe or ingrediant types
def choice_RI_type(choice_type, recipe_type, ingrediant_type):
    if choice_type == 1:
        info_type = recipe_type
    else:
        info_type = ingrediant_type
    return info_type


# Lists either the recipe or ingrediants by choice_type
def type_list(info_type, choice_type, main_dict):
    print(f'\nSelect a {main_dict[choice_type]} Type')
    for x in range(0, len(info_type)):
        print(f'\t{x}) {info_type[x]}')
    return len(info_type)


# Add a recipe or ingrediant to the respective csv file
def add_data(info_type, choice_type, main_dict, recipes, ingrediants):
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





