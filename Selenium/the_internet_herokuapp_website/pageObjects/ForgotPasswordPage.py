"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""

from selenium.webdriver.common.by import By


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver

    forgot_LinkText = (By.XPATH, "//a[text()='Forgot Password']")
    forgot_Header = (By.XPATH, "//h3[text()='Forgot Password']")

    # todo - email path
    forgot_EmailField = (By.XPATH, "")
    # todo - retrieve path
    forgot_Retrieve = (By.XPATH, "")


    def forgotPassword_Link(self):
        return self.driver.find_element(*ForgotPasswordPage.forgot_LinkText)

    def forgotPassword_HeaderText(self):
        return self.driver.find_element(*ForgotPasswordPage.forgot_Header)

    def forgotPassword_EmailField(self):
        return self.driver.find_element(*ForgotPasswordPage.forgot_EmailField)

    def forgotPassword_RetrieveButton(self):
        return self.driver.find_element(*ForgotPasswordPage.forgot_Retrieve)
