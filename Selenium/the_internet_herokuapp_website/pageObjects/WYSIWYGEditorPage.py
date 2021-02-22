"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

class WYSIWYGEditorPage:
    def __init__(self, driver):
        self.driver = driver

    wysiwyg_LinkText = (By.XPATH, "//a[text()='WYSIWYG Editor']")
    wysiwyg_Header = (By.XPATH, "//h3[text()='WYSIWYG Editor']")

    # todo - Area
    wysiwyg_Area = (By.XPATH, " ")

    # todo - all other options


    def WYSIWYGEditor_Link(self):
        return self.driver.find_element(*WYSIWYGEditorPage.wysiwyg_LinkText)

    def WYSIWYGEditor_HeaderText(self):
        return self.driver.find_element(*WYSIWYGEditorPage.wysiwyg_Header)

    def WYSIWYGEditor_Area(self):
        return self.driver.find_element(*WYSIWYGEditorPage.wysiwyg_Area)

