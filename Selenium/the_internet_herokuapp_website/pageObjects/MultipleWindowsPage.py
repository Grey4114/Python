"""
Website:  https://the-internet.herokuapp.com/windows
Created:  2/15/2021
Notes:
    Connected Test Object Script - /tests/test_Page_MultipleWindows.py
"""

from selenium.webdriver.common.by import By

class MultipleWindowsPage:
    def __init__(self, driver):
        self.driver = driver

    multiple_Link = (By.XPATH, "//a[text()='Multiple Windows']")            # Main Page link
    multiple_Header = (By.XPATH, "//h3[text()='Opening a new window']")     # Page header text
    multiple_Click = (By.XPATH, "//a[@href='/windows/new']")                # click here link
    multiple_NewHeader = (By.XPATH, "//h3[text()='New Window']")            # New page header path


    def multipleWindows_LinkText(self):
        return self.driver.find_element(*MultipleWindowsPage.multiple_Link)

    def multipleWindows_HeaderText(self):
        return self.driver.find_element(*MultipleWindowsPage.multiple_Header)

    def multipleWindows_ClickHere(self):
        return self.driver.find_element(*MultipleWindowsPage.multiple_Click)

    def multipleWindows_NewHeader(self):
        return self.driver.find_element(*MultipleWindowsPage.multiple_NewHeader)


