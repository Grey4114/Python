"""
Author: Chris Caprio
Program: Recipe Creator
Notes: This is the Functions section of the original recipe_creator_main.py script
"""

" --- IMPORTS --- "
import csv

" --- VARIABLES --- "
recipes_file = "D:\\GitHub\\Python\\Unittest\\recipe_creator_program\\recipes.csv"
ingrediants_file = "D:\\GitHub\\Python\\Unittest\\recipe_creator_program\\ingrediants.csv"

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
