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
    digest_Success = (By.XPATH, "//p[contains(text(),'Congratulations')]")  # Successful login text
    digest_Failed = (By.XPATH, "//h1[normalize-space()='Not Found']")  # Failed login text


    def digestAuth_LinkText(self):
        return self.driver.find_element(*DigestAuthPage.digest_Link)

    def digestAuth_SuccessLogin(self):
        return self.driver.find_element(*DigestAuthPage.digest_Success)


    def digestAuth_FailedLogin(self):
        return self.driver.find_element(*DigestAuthPage.digest_Failed)


