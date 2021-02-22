"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

# username: tomsmith
# password: SuperSecretPassword!

class FormAuthPage:
    def __init__(self, driver):
        self.driver = driver

    form_LinkText = (By.XPATH, "//a[text()='Form Authentication']")
    form_Header = (By.XPATH, "//h3[text()='Login Page']")

    # todo - user path
    form_User = (By.XPATH, " ")
    # todo - password path
    form_Pass = (By.XPATH, " ")
    # todo - login path
    form_Login = (By.XPATH, " ")
    # todo - valid path
    form_Valid = (By.XPATH, " ")
    # todo - invalid path
    form_Invalid = (By.XPATH, " ")


    def formAuth_Link(self):
        return self.driver.find_element(*FormAuthPage.form_LinkText)

    def formAuth_HeaderText(self):
        return self.driver.find_element(*FormAuthPage.form_Header)

    def formAuth_Username(self):
        return self.driver.find_element(*FormAuthPage.form_User)

    def formAuth_Password(self):
        return self.driver.find_element(*FormAuthPage.form_Pass)

    def formAuth_LoginButton(self):
        return self.driver.find_element(*FormAuthPage.form_Login)

    def formAuth_ValidText(self):
        return self.driver.find_element(*FormAuthPage.form_Valid)

    def formAuth_InvalidText(self):
        return self.driver.find_element(*FormAuthPage.form_Invalid)


