"""
Website:  https://the-internet.herokuapp.com/basic_auth
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_BasicAuth.py

    - user and pass: admin
    - No page header text
    - Apparently there is only one way to test this type of pop-up Auth window
    - According to the internet there is no way to test cancel button or false user/pass for the pop-up Auth window

    ** Digest Authentication & Secure File Download pages have the same issues as this page
"""

from selenium.webdriver.common.by import By

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

