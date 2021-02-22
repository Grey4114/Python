"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""

from selenium.webdriver.common.by import By

class FloatingMenuPage:
    def __init__(self, driver):
        self.driver = driver

    floating_LinkText = (By.XPATH, "//a[text()='Floating Menu']")
    floating_Header = (By.XPATH, "//h3[text()='Floating Menu']")

    # todo - scroll path
    floating_Scroll = (By.XPATH, "")


    def floatingMenu_Link(self):
        return self.driver.find_element(*FloatingMenuPage.floating_LinkText)

    def floatingMenu_HeaderText(self):
        return self.driver.find_element(*FloatingMenuPage.floating_Header)

    def floatingMenuScroll(self):
        return self.driver.find_element(*FloatingMenuPage.floating_Scroll)

