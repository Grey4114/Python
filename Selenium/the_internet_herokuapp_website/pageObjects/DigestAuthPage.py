"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Digest Authorization page
"""

from selenium.webdriver.common.by import By

# user and pass: admin

class DigestAuthPage:

    def __init__(self, driver):
        self.driver = driver

    digest_Link = (By.XPATH, "//a[text()='Digest Authentication']")     # Main Page link


    digest_Header = (By.XPATH, "//h3[text()='xxxxx']")      # todo - Page header text
    digest_User = (By.XPATH, "")                            # todo - user path
    digest_Pass = (By.XPATH, "")                            # todo - pass path
    digest_SignIn = (By.XPATH, "")                          # todo - sign in button
    digest_Cancel = (By.XPATH, "")                          # todo - cancel button
    digest_Failed = (By.XPATH, "")                          # todo - login failed text


    def digestAuth_LinkText(self):
        return self.driver.find_element(*DigestAuthPage.digest_Link)

    def digestAuth_HeaderText(self):
        return self.driver.find_element(*DigestAuthPage.digest_Header)

    def digestAuth_UserField(self):
        return self.driver.find_element(*DigestAuthPage.digest_User)

    def digestAuth_PassField(self):
        return self.driver.find_element(*DigestAuthPage.digest_Pass)

    def digestAuth_SignInButton(self):
        return self.driver.find_element(*DigestAuthPage.digest_SignIn)

    def digestAuth_CancelButton(self):
        return self.driver.find_element(*DigestAuthPage.digest_Cancel)

    def digestAuth_FailedLogin(self):
        return self.driver.find_element(*DigestAuthPage.digest_Failed)


