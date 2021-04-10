"""
Website:  https://the-internet.herokuapp.com/digest_auth
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_DigestAuth.py

    - user and pass: admin
    - No page header text
    - Apparently there is only one way to test this type of pop-up Auth window
    - According to the internet there is no way to test cancel button or false user/pass for the pop-up Auth window

    ** Basic Auth & Secure File Download pages have the same issues as this page
"""

from selenium.webdriver.common.by import By

class DigestAuthPage:

    def __init__(self, driver):
        self.driver = driver

    digest_Link = (By.XPATH, "//a[text()='Digest Authentication']")     # Main Page link
    digest_Success = (By.XPATH, "//p[contains(text(),'Congratulations')]")  # Successful login text
    digest_Failed = (By.XPATH, "//h1[normalize-space()='Not Found']")  # Failed login text


    def digestAuth_LinkText(self):
        return self.driver.find_element(*DigestAuthPage.digest_Link)

    def digestAuth_SuccessLogin(self):
        return self.driver.find_element(*DigestAuthPage.digest_Success)


    def digestAuth_FailedLogin(self):
        return self.driver.find_element(*DigestAuthPage.digest_Failed)


