"""
Website:  https://the-internet.herokuapp.com/nested_frames
Created:  2/15/2021
Notes:
    Connected Test Object Script - /tests/test_Page_NestedFrames.py
"""

from selenium.webdriver.common.by import By

class NestedFramesPage:
    def __init__(self, driver):
        self.driver = driver

    nested_Link = (By.XPATH, "//a[text()='Nested Frames']")     # Main Page link
    nested_Header = (By.XPATH, "//h3[text()='Nested Frames']")      # Page header text
    nested_Body = (By.XPATH, "/html/body")     # Gets the body info for any frame


    def nestedFrames_LinkText(self):
        return self.driver.find_element(*NestedFramesPage.nested_Link)

    def nestedFrames_HeaderText(self):
        return self.driver.find_element(*NestedFramesPage.nested_Header)

    def nestedFrames_BodyText(self):
        return self.driver.find_element(*NestedFramesPage.nested_Body)





