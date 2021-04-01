"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Basic Auth page
"""

from selenium.webdriver.common.by import By

# NOTE - user and pass: admin

class BasicAuthPage:
    def __init__(self, driver):
        self.driver = driver


    basic_Link = (By.XPATH, "//a[text()='Basic Auth']")                     # Main Website link to page
    basic_Success = (By.XPATH, "//p[contains(text(),'Congratulations! ')]")  # Success text
    basic_NotAuth = (By.XPATH, "//body[contains(text(),'Not authorized')]")  # Not Authorized text


    def basicAuth_LinkText(self):
        return self.driver.find_element(*BasicAuthPage.basic_Link)

    def basicAuth_SuccessText(self):
        return self.driver.find_element(*BasicAuthPage.basic_Success)

    def basicAuth_NotAuthorizedText(self):
        return self.driver.find_element(*BasicAuthPage.basic_NotAuth)


