"""
Author: Chris Caprio
Program: Recipe Creator
Notes: Unittest of the recipe_creator_classes.py script
"""

" --- IMPORTS --- "

import sys
import unittest
from io import StringIO
from recipe_creator_classes import Recipes, recipe_type, recipes_file
from recipe_creator_classes import main_dict, menu_dict
recipes_file = "D:\\GitHub\\Python\\Unittest\\recipe_creator_program\\recipes.csv"
recipes_test_file = "D:\\GitHub\\Python\\Unittest\\recipe_creator_program\\recipes_test.csv"
recipes_test_text = ['Cake', 'Chocolate Cake', 'milk', 'sugar']
recipe_info_test = ('Test', 'Chocolate Cake', 'milk')
recipes_write_text = ['Test', 'Chocolate Cake', 'milk']

" --- TEST CASES --- "
# Tests the Recipe Class
class TestRecipeClass(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.recipe = Recipes(recipe_type, recipes_file, main_dict, menu_dict)
        self.recipe_test = Recipes(recipe_type, recipes_test_file, main_dict, menu_dict)

    # Test opening/importing recipe csv file info
    def test_read_recipes_file(self):
        data = self.recipe_test.read_recipes_file()
        self.assertEqual(data[1], recipes_test_text)

    # Test writing a new line to the recipe csv file
    def test_write_recipes_file(self):
        self.recipe_test.write_recipes_file(recipe_info_test)
        data = self.recipe_test.read_recipes_file()
        self.assertEqual(data[-1], recipes_write_text)

    # Test list_recipes_all modules output text
    def test_list_recipes_all_text(self):
        data = self.recipe.read_recipes_file()
        self.recipe.list_recipes_all(data)
        self.assertEqual(sys.stdout.getvalue().strip(), "All Recipes"
                                                        "\n--------------"
                                                        "\n\t1) Chocolate Cake - Cake"
                                                        "\n\t2) Apple Pie - Pie"
                                                        "\n\t3) Tomato Soup - Soup"
                                                        "\n\t4) Rumble Cookie - Cookie"
                                                        "\n\t5) Gummy - Candy"
                                                        "\n\t6) Ham And Cheese - Sandwich")

    # Test list_recipes_all modules output results
    def test_list_recipes_all_results(self):
        data = self.recipe.read_recipes_file()
        self.assertEqual(self.recipe.list_recipes_all(data), 7)

    # Test list_recipes_type modules output text
    def test_list_recipes_type_text(self):
        data = self.recipe.read_recipes_file()
        self.recipe.list_recipes_type("Soup", data)
        self.assertEqual(sys.stdout.getvalue().strip(), "Soup Recipes"
                                                        "\n--------------"
                                                        "\n\t1) Tomato Soup")

    # Test list_recipes_type modules output results
    def test_list_recipes_type_results(self):
        data = self.recipe.read_recipes_file()
        self.assertEqual(self.recipe.list_recipes_type("Soup", data), (7, [3]))

    # Test list_full_recipe modules output text
    def test_list_full_recipe_text(self):
        data = self.recipe.read_recipes_file()
        self.recipe.list_full_recipe(3, data)
        self.assertEqual(sys.stdout.getvalue().strip(), "Tomato Soup Recipe"
                                                        "\n-------------------------"
                                                        "\n\tBanana"
                                                        "\n\tMustard")

    def tearDown(self):
        self.recipe = None


if __name__ == '__main__':
    unittest.main()
