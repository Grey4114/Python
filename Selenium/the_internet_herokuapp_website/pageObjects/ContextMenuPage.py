"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the ContextMenu page
"""

from selenium.webdriver.common.by import By

class ContextMenuPage:
    def __init__(self, driver):
        self.driver = driver

    context_Link = (By.XPATH, "//a[text()='Context Menu']")         # Main Page link
    context_Header = (By.XPATH, "//h3[text()='Context Menu']")      # Page header text
    context_Box = (By.XPATH, "//div[@id='hot-spot']")               # right click box


    def contextMenu_LinkText(self):
        return self.driver.find_element(*ContextMenuPage.context_Link)

    def contextMenu_HeaderText(self):
        return self.driver.find_element(*ContextMenuPage.context_Header)

    def contextMenu_RightClickBox(self):
        return self.driver.find_element(*ContextMenuPage.context_Box)

