"""
Author: Chris Caprio
Program: Recipe Creator
Notes: Unittest of the recipe_creator_functions.py script
"""

" --- IMPORTS --- "
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from recipe_creator_functions import welcome, main_menu, general_menu, menu_choice, choice_RI_type, type_list, add_data
from recipe_creator_classes import main_dict, menu_dict, ingrediant_type, recipe_type


" --- TEST CASES --- "
# Tests the Welcome function
class TestWelcome(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.welcome = welcome()

    def test_welcome_text(self):
        self.welcome
        self.assertEqual(sys.stdout.getvalue().strip(), "Welcome to the Recipe Manager"
                                                        "\n\tView and add ingrediants and recipes.")

    def tearDown(self):
        self.welcome = None

# Tests the Main Menu function
class TestMainMenu(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.main_menu = main_menu(main_dict)

    def test_main_menu_text(self):
        self.main_menu
        self.assertEqual(sys.stdout.getvalue().strip(), "Main Menu"
                                                        "\n------------" 
                                                        "\n\t1) Recipe" 
                                                        "\n\t2) Ingrediants" 
                                                        "\n\t3) Exit")

    def test_main_menu_return(self):
        self.assertEqual(self.main_menu, 3)

    def tearDown(self):
        self.main_menu = None

# Tests the General Menu function
class TestGeneralMenu(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_recipe_menu_text(self):
        general_menu('Recipe', menu_dict)
        self.assertEqual(sys.stdout.getvalue().strip(), "Recipe Menu"
                                                        "\n------------------"
                                                        "\n\t1) View All"
                                                        "\n\t2) Find By Type"
                                                        "\n\t3) Add"
                                                        "\n\t4) Main Menu")

    def test_recipe_menu_return(self):
        self.assertEqual(general_menu('Recipe', menu_dict), 4)

    def test_ingrediant_menu_text(self):
        general_menu('Ingrediants', menu_dict)
        self.assertEqual(sys.stdout.getvalue().strip(), "Ingrediants Menu"
                                                        "\n------------------"
                                                        "\n\t1) View All"
                                                        "\n\t2) Find By Type"
                                                        "\n\t3) Add"
                                                        "\n\t4) Main Menu")

    def test_ingrediant_menu_return(self):
        self.assertEqual(general_menu('Ingrediants', menu_dict), 4)

    def tearDown(self):
        pass

# Tests the Menu Choice function
class TestMenuChoice(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    @patch('builtins.input', return_value=1)
    def test_menu_choice_fist(self, mock_input):
        answer = menu_choice(3)
        self.assertEqual(answer, 1)

    @patch('builtins.input', return_value=3)
    def test_menu_choice_last(self, mock_input):
        answer = menu_choice(3)
        self.assertEqual(answer, 3)

    # Todo - invalid 0
    @patch('builtins.input', return_value=0)
    def test_menu_choice_invalid_0(self, mock_input):
        menu_choice(3)
        with self.assertRaises(ValueError):
            self.assertEqual(sys.stdout.getvalue().strip(), 'Value Error! Enter a valid number')

    # Todo - invalid 4
    @patch('builtins.input', return_value=4)
    def test_menu_choice_invalid_4(self, mock_input):
        answer = menu_choice(3)
        self.assertEqual(answer, 4)

    # Todo - invalid 'a'
    @patch('builtins.input', return_value='a')
    def test_menu_choice_invalid_letter(self, mock_input):
        menu_choice(3)
        self.assertEqual(sys.stdout.getvalue().strip(), "Select an Option: ")

    # Todo - invalid space
    @patch('builtins.input', return_value=' ')
    def test_menu_choice_invalid_none(self, mock_input):
        menu_choice(3)
        self.assertEqual(sys.stdout.getvalue().strip(), "Select an Option: ")

    def tearDown(self):
        pass

# Tests the Choice RI Type function
class TestChoiceRIType(unittest.TestCase):
    def setUp(self):
        self.choice_RI_type_1 = choice_RI_type(1, recipe_type, ingrediant_type)
        self.choice_RI_type_2 = choice_RI_type(2, recipe_type, ingrediant_type)

    def test_choice_type_recipe(self):
        self.assertEqual(self.choice_RI_type_1, recipe_type)

    def test_choice_type_ingrediant(self):
        self.assertEqual(self.choice_RI_type_2, ingrediant_type)

    def tearDown(self):
        self.choice_RI_type_1 = None
        self.choice_RI_type_2 = None

# Tests the Type List function
class TestTypeList(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_recipe_type_list(self):
        type_list(recipe_type, 1, main_dict)
        self.assertEqual(sys.stdout.getvalue().strip(), "Select a Recipe Type"
                                                        "\n\t0) Main Meal"
                                                        "\n\t1) Candy"
                                                        "\n\t2) Cookie"
                                                        "\n\t3) Cake"
                                                        "\n\t4) Pie"
                                                        "\n\t5) Soup"
                                                        "\n\t6) Sandwich"
                                                        "\n\t7) Salad")

    def test_ingrediants_type_list(self):
        type_list(ingrediant_type, 2, main_dict)
        self.assertEqual(sys.stdout.getvalue().strip(), "Select a Ingrediants Type"
                                                        "\n\t0) Spice"
                                                        "\n\t1) Fruit"
                                                        "\n\t2) Vegitable"
                                                        "\n\t3) Condiment"
                                                        "\n\t4) Protien"
                                                        "\n\t5) Grains")

    def test_recipe_type_return(self):
        self.assertEqual(type_list(recipe_type, 1, main_dict), 8)

    def test_ingrediant_type_return(self):
        self.assertEqual(type_list(ingrediant_type, 2, main_dict), 6)

    def tearDown(self):
        pass

# Todo - Do Add Data Tests
# Tests the Add Data function
class TestAddData(unittest.TestCase):
    def setUp(self):
        self.add_data_R = add_data(info_type, 1, main_dict, recipes, ingrediants)
        self.add_data_I = add_data(info_type, 2, main_dict, recipes, ingrediants)
        pass

    def test_number_1(self):
        self.assertEqual(True, True)

    def test_number_2(self):
        self.assertEqual(True, True)

    def test_number_3(self):
        self.assertEqual(True, True)

    def tearDown(self):
        self.add_data = None


if __name__ == '__main__':
    unittest.main()
