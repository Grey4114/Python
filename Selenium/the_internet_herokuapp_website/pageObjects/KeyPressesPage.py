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

    keyPress_Link = (By.XPATH, "//a[text()='Key Presses']")     # Main Page link
    keyPress_Header = (By.XPATH, "//h3[text()='Key Presses']")      # Page header text
    keyPress_Field = (By.ID, "target")    # Text field
    keyPress_Text = (By.ID, "result")     # Shows the key press entered


    def keyPresses_LinkText(self):
        return self.driver.find_element(*KeyPressesPage.keyPress_Link)

    def keyPresses_HeaderText(self):
        return self.driver.find_element(*KeyPressesPage.keyPress_Header)

    def keyPresses_Field(self):
        return self.driver.find_element(*KeyPressesPage.keyPress_Field)

    def keyPresses_Text(self):
        return self.driver.find_element(*KeyPressesPage.keyPress_Text)

