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

    drop_Link = (By.XPATH, "//a[text()='Dropdown']")            # Main Page link
    drop_Header = (By.XPATH, "//h3[text()='Dropdown List']")    # Page header text
    drop_List = (By.XPATH, "//select[@id='dropdown']/option")   # dropdown list path


    def dropDown_LinkText(self):
        return self.driver.find_element(*DropDownPage.drop_Link)

    def dropDown_HeaderText(self):
        return self.driver.find_element(*DropDownPage.drop_Header)

    def dropDown_List(self):
        return self.driver.find_elements(*DropDownPage.drop_List)


