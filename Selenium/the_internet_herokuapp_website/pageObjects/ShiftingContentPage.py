"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


class ShiftingContentPage:
    def __init__(self, driver):
        self.driver = driver

    shifting_LinkText = (By.XPATH, "//a[text()='Shifting Content']")
    shifting_Header = (By.XPATH, "//h3[text()='Shifting Content']")

    # todo - menu element
    shifting_Menu = (By.XPATH, " ")
    # todo - Images
    shifting_Image = (By.XPATH, " ")
    # todo - List
    shifting_List = (By.XPATH, " ")


    # todo - example 1 - Header
    example1_Header = (By.XPATH, " ")
    # todo - example 1 - URL
    example1_URL = (By.XPATH, " ")
    # todo - example 1 - Shift
    example1_Shift = (By.XPATH, " ")
    # todo - example 1 - Random
    example1_Random = (By.XPATH, " ")


    # todo - example 2 - Header
    example2_Header = (By.XPATH, " ")
    # todo - example 2 - URL
    example2_URL = (By.XPATH, " ")
    # todo - example 2 - shift
    example2_Shift = (By.XPATH, " ")
    # todo - example 2 - Random
    example2_Random = (By.XPATH, " ")
    # todo - example 2 - Simple Image
    example2_Simple = (By.XPATH, " ")


    # todo - example 3 - Header
    example3_Header = (By.XPATH, " ")
    # todo - example 3 - Text
    example3_Text = (By.XPATH, " ")


    def shiftingContent_Link(self):
        return self.driver.find_element(*ShiftingContentPage.shifting_LinkText)

    def shiftingContent_HeaderText(self):
        return self.driver.find_element(*ShiftingContentPage.shifting_Header)

    def shiftingContent_MenuElemnt(self):
        return self.driver.find_element(*ShiftingContentPage.shifting_Menu)

    def shiftingContent_AnImage(self):
        return self.driver.find_element(*ShiftingContentPage.shifting_Image)

    def shiftingContent_List(self):
        return self.driver.find_element(*ShiftingContentPage.shifting_List)



    def shiftingContent_Example1_HeaderText(self):
        return self.driver.find_element(*ShiftingContentPage.example1_Header)

    def shiftingContent_Example1_URL(self):
        return self.driver.find_element(*ShiftingContentPage.example1_URL)

    def shiftingContent_Example1_Shift(self):
        return self.driver.find_element(*ShiftingContentPage.example1_Shift)

    def shiftingContent_Example1_Random(self):
        return self.driver.find_element(*ShiftingContentPage.example1_Random)



    def shiftingContent_Example2_HeaderText(self):
        return self.driver.find_element(*ShiftingContentPage.example2_Header)

    def shiftingContent_Example2_URL(self):
        return self.driver.find_element(*ShiftingContentPage.example2_URL)

    def shiftingContent_Example2_Shift(self):
        return self.driver.find_element(*ShiftingContentPage.example2_Shift)

    def shiftingContent_Example2_Random(self):
        return self.driver.find_element(*ShiftingContentPage.example2_Random)

    def shiftingContent_Example2_Simple(self):
        return self.driver.find_element(*ShiftingContentPage.example2_Simple)



    def shiftingContent_Example3_HeaderText(self):
        return self.driver.find_element(*ShiftingContentPage.example3_Header)

    def shiftingContent_Example3_Text(self):
        return self.driver.find_element(*ShiftingContentPage.example3_Text)

