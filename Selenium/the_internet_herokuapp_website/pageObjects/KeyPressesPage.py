"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

class KeyPressesPage:
    def __init__(self, driver):
        self.driver = driver

    keyPress_LinkText = (By.XPATH, "//a[text()='Key Presses']")
    keyPress_Header = (By.XPATH, "//h3[text()='Key Presses']")

    # todo - field path
    keyPress_Field = (By.XPATH, " ")
    # todo - Text path
    keyPress_Text = (By.XPATH, " ")


    def keyPresses_Link(self):
        return self.driver.find_element(*KeyPressesPage.keyPress_LinkText)

    def keyPresses_HeaderText(self):
        return self.driver.find_element(*KeyPressesPage.keyPress_Header)

    def keyPresses_Field(self):
        return self.driver.find_element(*KeyPressesPage.keyPress_Field)

    def keyPresses_Text(self):
        return self.driver.find_element(*KeyPressesPage.keyPress_Text)

