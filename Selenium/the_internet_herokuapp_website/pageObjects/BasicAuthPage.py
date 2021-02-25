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
    basic_Header = (By.XPATH, "//h3[text()='Add/Remove Elements']")         # Page header text

    basic_Name = (By.XPATH, " ")    # todo - alert name
    basic_Pass = (By.XPATH, " ")    # todo - alert password
    basic_Sign = (By.XPATH, " ")    # todo - alert Sign In Button
    basic_Cancel = (By.XPATH, " ")    # todo - alert Cancel Button
    basic_Success = (By.XPATH, " ")  # todo - Success text
    basic_NotAuth = (By.XPATH, "//body[contains(text(),'Not authorized')]")  # Not Authorized text



    def basicAuth_LinkText(self):
        return self.driver.find_element(*BasicAuthPage.basic_Link)

    def basicAuth_HeaderText(self):
        return self.driver.find_element(*BasicAuthPage.basic_Header)

    def basicAuth_UserName(self):
        return self.driver.find_element(*BasicAuthPage.basic_Name)

    def basicAuth_Password(self):
        return self.driver.find_element(*BasicAuthPage.basic_Pass)

    def basicAuth_SignInButton(self):
        return self.driver.find_element(*BasicAuthPage.basic_Sign)

    def basicAuth_CancelButton(self):
        return self.driver.find_element(*BasicAuthPage.basic_Cancel)

    def basicAuth_SuccessText(self):
        return self.driver.find_element(*BasicAuthPage.basic_Success)

    def basicAuth_NotAuthorizedText(self):
        return self.driver.find_element(*BasicAuthPage.basic_NotAuth)


