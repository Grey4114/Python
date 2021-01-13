"""
Author: Chris Caprio
Program: Recipe Creator
Details:
Create a recipe class with ingredients and a put them in a recipe manager program that organizes them into
categories like deserts, main courses or by ingredients like chicken, beef, soups, pies etc.
"""

" --- IMPORTS --- "
from recipe_creator_functions import welcome, main_menu, general_menu, add_data, menu_choice,choice_RI_type, type_list
from recipe_creator_classes import recipes_file, recipe_type, ingrediant_type, ingrediants_file, main_dict, menu_dict
from recipe_creator_classes import Recipes, Ingrediants


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
            # info_type = choice_RI_type(choice_type, recipes, ingrediants, recipe_type, ingrediant_type)
            info_type = choice_RI_type(choice_type, recipe_type, ingrediant_type)

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
                add_data(info_type, choice_type, main_dict, recipes, ingrediants)
                input('\nPress any key to return to the Main Menu ')
                looping = False
            else:
                break


" --- NAME SPACE --- "
if __name__ == "__main__":
    welcome()
    main()
    print('\nThanks for playing!')


