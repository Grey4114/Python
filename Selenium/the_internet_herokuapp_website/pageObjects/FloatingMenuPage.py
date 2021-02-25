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

    floating_LinkText = (By.XPATH, "//a[text()='Floating Menu']")       # Main Page link
    floating_Header = (By.XPATH, "//h3[text()='Floating Menu']")        # Page header text

    floating_Page = (By.TAG_NAME, "html")                               # Webpage Info
    floating_Scroll = (By.XPATH, "//div[@id='menu']")                   # Menu / Scroll page info
    floating_Home = (By.XPATH, "//a[@href='#home']")                    # Home button
    floating_News = (By.XPATH, "//a[@href='#news']")                    # News button
    floating_Contact = (By.XPATH, "//a[@href='#contact']")              # Contact button
    floating_About = (By.XPATH, "//a[@href='#about']")                  # About button


    def floatingMenu_Link(self):
        return self.driver.find_element(*FloatingMenuPage.floating_LinkText)

    def floatingMenu_HeaderText(self):
        return self.driver.find_element(*FloatingMenuPage.floating_Header)

    def floatingMenu_PageInfo(self):
        return self.driver.find_element(*FloatingMenuPage.floating_Page)

    def floatingMenu_Scroll(self):
        return self.driver.find_element(*FloatingMenuPage.floating_Scroll)

    def floatingMenu_HomeButton(self):
        return self.driver.find_element(*FloatingMenuPage.floating_Home)

    def floatingMenu_NewsButton(self):
        return self.driver.find_element(*FloatingMenuPage.floating_News)

    def floatingMenu_ContactButton(self):
        return self.driver.find_element(*FloatingMenuPage.floating_Contact)

    def floatingMenu_AboutButton(self):
        return self.driver.find_element(*FloatingMenuPage.floating_About)

