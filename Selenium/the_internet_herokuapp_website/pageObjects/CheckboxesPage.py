"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Checkboxes page
"""

from selenium.webdriver.common.by import By


class CheckboxesPage:
    def __init__(self, driver):
        self.driver = driver

    check_LinkText = (By.XPATH, "//a[text()='Checkboxes']")
    check_Header = (By.XPATH, "//h3[text()='Checkboxes']")
    check_Boxes = (By.XPATH, "//input[@type='checkbox']")
    checked = (By.CSS_SELECTOR, "input:checked[type='checkbox']")   # Checks if the boxes are checked
    notchecked = (By.CSS_SELECTOR, "input:not(:checked)[type='checkbox']")  # Checks if the boxes are not checked


    def checkboxes_Link(self):
        return self.driver.find_element(*CheckboxesPage.check_LinkText)

    def checkbox_HeaderText(self):
        return self.driver.find_element(*CheckboxesPage.check_Header)

    def checkbox_Boxes(self):
        return self.driver.find_elements(*CheckboxesPage.check_Boxes)

    def checked_Boxes(self):
        return self.driver.find_elements(*CheckboxesPage.checked)

    def notchecked_Boxes(self):
        return self.driver.find_elements(*CheckboxesPage.notchecked)

