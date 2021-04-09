"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""

from selenium.webdriver.common.by import By

class FramesPage:
    def __init__(self, driver):
        self.driver = driver

    frames_Link = (By.XPATH, "//a[text()='Frames']")        # Main Page link
    frames_Header = (By.XPATH, "//h3[text()='Frames']")         # Page header text


    def frames_LinkText(self):
        return self.driver.find_element(*FramesPage.frames_Link)

    def frames_HeaderText(self):
        return self.driver.find_element(*FramesPage.frames_Header)





