"""
Author: Chris Caprio
Program: Recipe Maker
Details:
Create a recipe class with ingredients and a put them in a recipe manager program that organizes them into
categories like deserts, main courses or by ingredients like chicken, beef, soups, pies etc.
Notes:
"""

" --- IMPORTS --- "
import csv



" --- VARIABLES --- "
recipes_file = "D:\\GitHub\\Python\\Standard\\recipe_creator\\recipes.csv"
ingrediants_file = "D:\\GitHub\\Python\\Standard\\recipe_creator\\ingrediants.csv"

recipe_type = ('Main Meal', 'Candy', 'Cookie', 'Cake', 'Pie', 'Soup', 'Sandwich', 'Salad')
ingrediant_type = ('Spice', 'Fruit', 'Vegitable', 'Condiment', 'Protien', 'Grains')

measurment = ('Cup', 'Teaspoon', 'Tablespoon')

main_dict = {1: 'Recipe', 2: 'Ingrediants', 3: 'Exit'}
menu_dict = {1: 'View All', 2: 'Find By Type', 3: 'Add', 4: 'Main Menu'}





" --- CLASSES --- "
# 
class Recipes:
    # todo - Delete a recipe
    # todo - Edit a recipe

    #
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
        print(f'\nRecipes')
        print(f'--------------')
        for x in range(1, len(recipe_data)):
            print(f'{recipe_data[x][0]}) {recipe_data[x][2]} - {recipe_data[x][1]}')

    # Prints a list of recipes by type
    def list_recipes_type(self, res_type, recipe_data):
        print(f'\n{res_type} Recipes')
        print(f'--------------')
        count = 0
        for x in range(1, len(recipe_data)):
            if recipe_data[x][1] == res_type:
                count += 1
                print(f'{count}) {recipe_data[x][2]} - {recipe_data[x][1]}')

    # Prints one full recipe and its ingrediants
    def list_full_recipe(self, res_num, recipe_data):
        print(f'\n{recipe_data[res_num][2]}')
        print(f'--------------')
        for x in range(3, len(recipe_data[res_num])):
            print(f'\t{recipe_data[res_num][x]}')

    def enter_new_recipe(self):
        pass

    def __str__(self):
        pass




#
class Ingrediants:
    # todo - Read ingrediant data from csv file
    # todo - Write new ingrediant data to csv file
    # todo - Print list of all ingrediant
    # todo - Print list of ingrediant types & # of ingrediant per type
    # todo - Print list ingrediant in a type
    # todo - Print a ingrediant
    # todo - Add a ingrediant
    # todo - Delete a ingrediant
    # todo - Edit a ingrediant

    #
    def __init__(self, ingrediant_type, ingrediants_file, main_dict, menu_dict):
        self.ingrediant_type = ingrediant_type
        self.ingrediants_file = ingrediants_file

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

    # Prints a full list of either the recipe or ingrediant data
    def view_info(choice_type, main_dict, data):
        print(f'\n{main_dict[choice_type]}')
        print(f'--------------')

        for x in range(1, len(data)):
            print(f'{data[x][0]}) {data[x][2]} - {data[x][1]}')

            if choice_type == 1:
                for info in range(3, len(data[x])):
                    print(f'\t{data[x][info]}')
                print('\n')



    def __str__(self):
        pass




" --- FUNCTIONS --- "
# This prints the startup info for the program
def welcome():
    print("\nWelcome to the Recipe Manager")
    print("\tAdd, edit, delete and view your recipes")
    input("\tPress any key to continue ")


# The main menu function
def main_menu():
    print("\nMain Menu")
    print("------------")
    print("\t1) Recipes")
    print("\t2) Ingrediants")
    print("\t3) Exit App")

    while True:
        try:
            choice = int(input("\tChoice: "))
            if choice < 1 or choice > 3:
                raise ValueError()
        except ValueError:
            print('\tValue Error! Enter a valid number')
            continue
        break
    return choice





# For Loop that prints out the menu
def general_menu(main_dict, menu_dict):
    print(f"\n{main_dict} Menu")
    print("------------------")
    for x in range(0, len(menu_dict)):
        print(f"\t{x+1}) {menu_dict[x+1]}")
    menu_choice(len(menu_dict))


# While loop - input choice for the general_menu function
def menu_choice(length):
    while True:
        try:
            choice = int(input("\tChoice: "))
            if choice < 1 or choice > length:
                raise ValueError()
        except ValueError:
            print('\tValue Error! Enter a valid number')
            continue
        break
    return choice
















"""




# Sets variables for either recipe or ingrediant types
def choice_RI_type(choice_type, recipe_type, ingrediant_type):
    if choice_type == 1:
        data = read_recipes_file()
        info_type = recipe_type
    else:
        data = read_ingrediants_file()
        info_type = ingrediant_type

    return data, info_type


# Lists either the recipe or ingrediants by choice_type
def type_list(info_type, choice_type, main_dict):
    print(f'Select a {main_dict[choice_type]} Type')
    for x in range(len(info_type)):
        print(f'\t{x+1}) {info_type[x]}')


# Prints a full list of either the recipe or ingrediant data
def view_info(choice_type, main_dict, data):
    print(f'\n{main_dict[choice_type]}')
    print(f'--------------')

    for x in range(1, len(data)):
        print(f'{data[x][0]}) {data[x][2]} - {data[x][1]}')

        if choice_type == 1:
            for info in range(3, len(data[x])):
                print(f'\t{data[x][info]}')
            print('\n')



# Add a recipe or ingrediant to the respective csv file
def add_data(info_type, choice_type, main_dict, data):
    add_info = []
    num = len(data)
    print(f'\n\nAdd {main_dict[choice_type]}')
    add_info.append(num)



    while True:
        type_list(info_type, choice_type, main_dict)
        type_choice = int(input('Choice: '))
        add_info.append(info_type[type_choice-1])

        name = input(f'\nEnter a {main_dict[choice_type]} name: ')
        add_info.append(name)



        if choice_type == 1:
            ingred = read_ingrediants_file()
            view_info(2, main_dict, ingred)
            add_ingred = int(input('Select an ingrediant: '))
            add_info.append(ingred[add_ingred][2])

            # yes_no = input('Add another ingrediant(y/n): ')
            write_recipes_file(add_info)

        else:
            write_ingrediants_file(add_info)



        print(add_info)

        break

"""





" --- MAIN FUNCTION --- "
def main():
    playing = True

    recipes = Recipes(recipe_type, recipes_file, main_dict, menu_dict)
    ingrediants = Ingrediants(ingrediant_type, ingrediants_file, main_dict, menu_dict)



    while True:
        recipe_data = recipes.read_recipes_file()
        ingrediant_data = ingrediants.read_ingrediants_file()

        welcome()
        choice = main_menu()

        while playing:
            general_menu(main_dict[choice], menu_dict)


            # choice_type = menu_choice(length)


            # recipes.list_recipes_all(recipe_data)

            #res_type = "Sandwich"
            #recipes.list_recipes_type(res_type, recipe_data)
            #res_num = 3
            #recipes.list_full_recipe(res_num, recipe_data)

            # data, info_type = choice_RI_type(choice_type, recipe_type, ingrediant_type)
            # general_menu(main_dict[choice_type], menu_dict)
            # view_info(choice_type, main_dict, data)
            # type_list(info_type, choice_type, main_dict)
            # add_data(info_type, choice_type, main_dict, data)

            playing = False
            break
        return playing




" --- NAME SPACE --- "
if __name__ == "__main__":
    playing = main()
    print('\nThanks for playing!')


