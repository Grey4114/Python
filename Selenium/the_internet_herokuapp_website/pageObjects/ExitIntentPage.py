"""
Website:  https://the-internet.herokuapp.com/exit_intent
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_ExitIntent.py
"""

from selenium.webdriver.common.by import By

class ExitIntentPage:
    def __init__(self, driver):
        self.driver = driver

    exit_Link = (By.XPATH, "//a[text()='Exit Intent']")         # Main Page link
    exit_Header = (By.XPATH, "//h3[text()='Exit Intent']")      # Page header text
    exit_Window = (By.XPATH, "//body")                          # Click outside webpage
    exit_Model = (By.XPATH, "//div[@class='modal-footer']")               # Modal window close
    exit_State = (By.XPATH, "//div[@id='modal']")                         # Modal window state



    def exitIntent_LinkText(self):
        return self.driver.find_element(*ExitIntentPage.exit_Link)

    def exitIntent_HeaderText(self):
        return self.driver.find_element(*ExitIntentPage.exit_Header)

    def exitIntent_WindowOutside(self):
        return self.driver.find_element(*ExitIntentPage.exit_Window)

    def exitIntent_ModalWindowClose(self):
        return self.driver.find_element(*ExitIntentPage.exit_Model)

    def exitIntent_ModalWindowSate(self):
        return self.driver.find_element(*ExitIntentPage.exit_State)
