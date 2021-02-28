"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

# user  and pass: admin

class SecureFileDownloadPage:
    def __init__(self, driver):
        self.driver = driver

    secure_Link = (By.XPATH, "//a[text()='Secure File Download']")      # Main Page link
    secure_Header = (By.XPATH, "//h3[text()='Secure File Download']")       # Page header text

    secure_User = (By.XPATH, " ")       # todo - user path

    secure_Pass = (By.XPATH, " ")       # todo - pass path

    secure_Sign = (By.XPATH, " ")       # todo - sign in path

    secure_Cancel = (By.XPATH, " ")     # todo - cancel path

    secure_Auth = (By.XPATH, " ")       # todo - auth text path



    def secureFileDownload_LinkText(self):
        return self.driver.find_element(*SecureFileDownloadPage.secure_Link)

    def secureFileDownload_HeaderText(self):
        return self.driver.find_element(*SecureFileDownloadPage.secure_Header)

    def secureFileDownload_Username(self):
        return self.driver.find_element(*SecureFileDownloadPage.secure_User)

    def secureFileDownload_Password(self):
        return self.driver.find_element(*SecureFileDownloadPage.secure_Pass)

    def secureFileDownload_SignIn(self):
        return self.driver.find_element(*SecureFileDownloadPage.secure_Sign)

    def secureFileDownload_Cancel(self):
        return self.driver.find_element(*SecureFileDownloadPage.secure_Cancel)

    def secureFileDownload_AuthText(self):
        return self.driver.find_element(*SecureFileDownloadPage.secure_Auth)

