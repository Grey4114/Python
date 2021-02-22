"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""

from selenium.webdriver.common.by import By


class ExitIntentPage:
    def __init__(self, driver):
        self.driver = driver

    exit_LinkText = (By.XPATH, "//a[text()='Exit Intent']")
    exit_Header = (By.XPATH, "//h3[text()='Exit Intent']")


    # todo - mouse path
    exit_Mouse = (By.XPATH, "")
    # todo - window header text path
    exit_WindowHeader = (By.XPATH, "")
    # todo - window close path
    exit_WindowClose = (By.XPATH, "")



    def exitIntent_Link(self):
        return self.driver.find_element(*ExitIntentPage.exit_LinkText)

    def exitIntent_HeaderText(self):
        return self.driver.find_element(*ExitIntentPage.exit_Header)

    def exitIntent_MouseOut(self):
        return self.driver.find_element(*ExitIntentPage.exit_Mouse)

    def exitIntent_WindowHeader(self):
        return self.driver.find_element(*ExitIntentPage.exit_WindowHeader)

    def exitIntent_WindowClose(self):
        return self.driver.find_element(*ExitIntentPage.exit_WindowClose)
