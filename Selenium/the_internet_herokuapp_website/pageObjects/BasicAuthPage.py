"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Basic Auth page
"""

from selenium.webdriver.common.by import By


# todo - verify being on page
# todo - select cancel and verify
# todo - Enter name, pass and accept, then verify


class BasicAuthPage:
    def __init__(self, driver):
        self.driver = driver

    basic_LinkText = (By.XPATH, "//a[text()='Basic Auth']")


    def basicAuth_Link(self):
        return self.driver.find_element(*BasicAuthPage.basic_LinkText)


