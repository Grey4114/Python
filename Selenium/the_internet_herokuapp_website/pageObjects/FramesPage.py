"""
Website:  https://the-internet.herokuapp.com/frames
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_Frames.py

    This page simply links to 2 other pages that already have test scripts writtem for them
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

