"""
Website:  https://the-internet.herokuapp.com/floating_menu
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_FloatingMenu.py
"""

from selenium.webdriver.common.by import By

class FloatingMenuPage:
    def __init__(self, driver):
        self.driver = driver

    floating_LinkText = (By.XPATH, "//a[text()='Floating Menu']")       # Main Page link
    floating_Header = (By.XPATH, "//h3[text()='Floating Menu']")        # Page header text
    floating_Body = (By.XPATH, "//body")                               # Webpage Info
    floating_Menu = (By.XPATH, "//div[@id='menu']")                    # Menu


    def floatingMenu_Link(self):
        return self.driver.find_element(*FloatingMenuPage.floating_LinkText)

    def floatingMenu_HeaderText(self):
        return self.driver.find_element(*FloatingMenuPage.floating_Header)

    def floatingMenu_PageBody(self):
        return self.driver.find_element(*FloatingMenuPage.floating_Body)

    def floatingMenu_PageMenu(self):
        return self.driver.find_element(*FloatingMenuPage.floating_Menu)


