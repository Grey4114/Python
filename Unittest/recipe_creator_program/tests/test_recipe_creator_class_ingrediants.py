"""
Author: Chris Caprio
Program: Recipe Creator
Notes: Unittest of the recipe_creator_classes.py script
"""

" --- IMPORTS --- "
import sys
import unittest
from io import StringIO
from recipe_creator_classes import Ingrediants, ingrediant_type, ingrediants_file
from recipe_creator_classes import main_dict, menu_dict
ingrediants_file = "D:\\GitHub\\Python\\Unittest\\recipe_creator_program\\ingrediants.csv"
ingrediants_test_file = "D:\\GitHub\\Python\\Unittest\\recipe_creator_program\\ingrediants_test.csv"
ingrediants_test_text = ['Spice', 'Salt']
ingrediants_info_test = ('Test', 'Vanilla')
ingrediants_write_text = ['Test', 'Vanilla']



" --- TEST CASES --- "
# Tests the Ingrediants Class
class TestIngrediantsClass(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.ingrediants = Ingrediants(ingrediant_type, ingrediants_file, main_dict, menu_dict)
        self.ingrediants_test = Ingrediants(ingrediant_type, ingrediants_test_file, main_dict, menu_dict)

    # Test opening/importing ingrediants csv file info
    def test_read_ingrediants_file(self):
        data = self.ingrediants_test.read_ingrediants_file()
        self.assertEqual(data[1], ingrediants_test_text)

    # Todo - Write to ingrediants file - Writing to wrong file, Not sure how to get this to work
    # Test writing a new line to the ingrediants csv file
    def test_write_ingrediants_file(self):
        self.ingrediants_test.write_ingrediants_file(ingrediants_info_test)
        data = self.ingrediants_test.read_ingrediants_file()
        self.assertEqual(data[-1], ingrediants_write_text)

    # Test list_ingrediants_all modules output text
    def test_list_ingrediants_all_text(self):
        data = self.ingrediants.read_ingrediants_file()
        self.ingrediants.list_ingrediants_all(data)
        self.assertEqual(sys.stdout.getvalue().strip(), "All Ingrediants"
                                                        "\n--------------"
                                                        "\n\t1) Salt - Spice"
                                                        "\n\t2) Pepper - Spice"
                                                        "\n\t3) Mustard - Condiment"
                                                        "\n\t4) Mayo - Condiment"
                                                        "\n\t5) Chicken - Protien"
                                                        "\n\t6) Steak - Protien"
                                                        "\n\t7) Apple - Fruit"
                                                        "\n\t8) Banana - Fruit"
                                                        "\n\t9) Tomato - Vegitable"
                                                        "\n\t10) Carrot - Vegitable")


    # Test list_ingrediants_all modules output results
    def test_list_ingrediants_all_results(self):
        data = self.ingrediants.read_ingrediants_file()
        self.assertEqual(self.ingrediants.list_ingrediants_all(data), 11)


    # Test list_ingrediants_type modules output text
    def test_list_ingrediants_type_text(self):
        data = self.ingrediants.read_ingrediants_file()
        self.ingrediants.list_ingrediants_type("Fruit", data)
        self.assertEqual(sys.stdout.getvalue().strip(), "Fruit Ingrediants"
                                                        "\n------------------------"
                                                        "\n\t1) Apple"
                                                        "\n\t2) Banana")

    # Test list_ingrediants_type modules output results
    def test_list_ingrediants_type_results(self):
        data = self.ingrediants.read_ingrediants_file()
        self.assertEqual(self.ingrediants.list_ingrediants_type("Fruit", data), 11)


    def tearDown(self):
        self.ingrediants = None


if __name__ == '__main__':
    unittest.main()
