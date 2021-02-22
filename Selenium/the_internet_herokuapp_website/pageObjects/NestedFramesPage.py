"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


class NestedFramesPage:
    def __init__(self, driver):
        self.driver = driver

    nested_LinkText = (By.XPATH, "//a[text()='Nested Frames']")
    nested_Header = (By.XPATH, "//h3[text()='Nested Frames']")

    # todo - nested right path
    nested_Right = (By.XPATH, " ")
    # todo - nested left path
    nested_Left = (By.XPATH, " ")
    # todo - nested bottom path
    nested_Bottom = (By.XPATH, " ")


    def nestedFrames_Link(self):
        return self.driver.find_element(*NestedFramesPage.nested_LinkText)

    def nestedFrames_HeaderText(self):
        return self.driver.find_element(*NestedFramesPage.nested_Header)

    def nestedFrames_Right(self):
        return self.driver.find_element(*NestedFramesPage.nested_Right)

    def nestedFrames_Left(self):
        return self.driver.find_element(*NestedFramesPage.nested_Left)

    def nestedFrames_Bottom(self):
        return self.driver.find_element(*NestedFramesPage.nested_Bottom)



