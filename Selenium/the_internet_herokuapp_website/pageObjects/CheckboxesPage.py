"""
Website:  https://the-internet.herokuapp.com/checkboxes
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_Checkboxes.py
"""

from selenium.webdriver.common.by import By


class CheckboxesPage:
    def __init__(self, driver):
        self.driver = driver

    check_Link = (By.XPATH, "//a[text()='Checkboxes']")                     # Main Page link
    check_Header = (By.XPATH, "//h3[text()='Checkboxes']")                  # Page header text
    check_Boxes = (By.XPATH, "//input[@type='checkbox']")                   # Check how many check boxes there are
    checked = (By.CSS_SELECTOR, "input:checked[type='checkbox']")           # Checks if the boxes are checked
    notchecked = (By.CSS_SELECTOR, "input:not(:checked)[type='checkbox']")  # Checks if the boxes are not checked


    def checkboxes_LinkText(self):
        return self.driver.find_element(*CheckboxesPage.check_Link)

    def checkbox_HeaderText(self):
        return self.driver.find_element(*CheckboxesPage.check_Header)

    def checkbox_Boxes(self):
        return self.driver.find_elements(*CheckboxesPage.check_Boxes)

    def checked_Boxes(self):
        return self.driver.find_elements(*CheckboxesPage.checked)

    def notchecked_Boxes(self):
        return self.driver.find_elements(*CheckboxesPage.notchecked)

