"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Broken Images page
"""

from selenium.webdriver.common.by import By

class BrokenImagePage:
    def __init__(self, driver):
        self.driver = driver

    broken_Link = (By.XPATH, "//a[text()='Broken Images']")            # Main Page link
    broken_Header = (By.XPATH, "//h3[text()='Broken Images']")         # Page header text
    broken_List = (By.TAG_NAME, "img")                                  # List of all images


    def broken_LinkText(self):
        return self.driver.find_element(*BrokenImagePage.broken_Link)

    def broken_HeaderText(self):
        return self.driver.find_element(*BrokenImagePage.broken_Header)

    def brokenImage_List(self):
        return self.driver.find_elements(*BrokenImagePage.broken_List)


