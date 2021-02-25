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

    forgot_Link = (By.XPATH, "//a[text()='Forgot Password']")       # Main Page link
    forgot_Header = (By.XPATH, "//h2[text()='Forgot Password']")        # Page header text
    forgot_Email = (By.XPATH, "//input[@id='email']")                   # Email field
    forgot_Retrieve = (By.XPATH, "//i[@class='icon-2x icon-signin']")   # Retrieve Button
    forgot_Error = (By.XPATH, "//h1[text()='Internal Server Error']")  # Error Text


    def forgotPassword_LinkText(self):
        return self.driver.find_element(*ForgotPasswordPage.forgot_Link)

    def forgotPassword_HeaderText(self):
        return self.driver.find_element(*ForgotPasswordPage.forgot_Header)

    def forgotPassword_EmailField(self):
        return self.driver.find_element(*ForgotPasswordPage.forgot_Email)

    def forgotPassword_RetrieveButton(self):
        return self.driver.find_element(*ForgotPasswordPage.forgot_Retrieve)

    def forgotPassword_InterServerError(self):
        return self.driver.find_element(*ForgotPasswordPage.forgot_Error)

