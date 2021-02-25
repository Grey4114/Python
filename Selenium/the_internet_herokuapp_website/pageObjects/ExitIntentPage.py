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

    exit_Link = (By.XPATH, "//a[text()='Exit Intent']")         # Main Page link
    exit_Header = (By.XPATH, "//h3[text()='Exit Intent']")      # Page header text

    exit_WindowHeader = (By.XPATH, "//h3[text()='This is a modal window']")     # Modal window header text
    exit_WindowClose = (By.XPATH, "//div[@class='modal-footer']")               # Modal window close
    exit_WindowState = (By.XPATH, "//div[@id='modal']")                         # Modal window state



    def exitIntent_LinkText(self):
        return self.driver.find_element(*ExitIntentPage.exit_Link)

    def exitIntent_HeaderText(self):
        return self.driver.find_element(*ExitIntentPage.exit_Header)

    def exitIntent_MouseOut(self):
        return self.driver.find_element(*ExitIntentPage.exit_Mouse)

    def exitIntent_ModalWindowHeader(self):
        return self.driver.find_element(*ExitIntentPage.exit_WindowHeader)

    def exitIntent_ModalWindowClose(self):
        return self.driver.find_element(*ExitIntentPage.exit_WindowClose)

    def exitIntent_ModalWindowSate(self):
        return self.driver.find_element(*ExitIntentPage.exit_WindowState)
