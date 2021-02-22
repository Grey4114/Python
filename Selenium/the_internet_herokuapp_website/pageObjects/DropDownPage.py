"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Drop Down page
"""

from selenium.webdriver.common.by import By

class DropDownPage:
    def __init__(self, driver):
        self.driver = driver

    drop_LinkText = (By.XPATH, "//a[text()='Dropdown']")
    drop_Header = (By.XPATH, "//h3[text()='Dropdown List']")

    # todo - dropdown list path
    drop_List = (By.XPATH, "")


    def dropDown_Link(self):
        return self.driver.find_element(*DropDownPage.drop_LinkText)

    def dropDown_HeaderText(self):
        return self.driver.find_element(*DropDownPage.drop_Header)

    def dropDown_List(self):
        return self.driver.find_elements(*DropDownPage.drop_List)


