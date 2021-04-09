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

    secure_Link = (By.XPATH, "//a[text()='Secure File Download']")          # Main Page link
    secure_Header = (By.XPATH, "//h3[normalize-space()='Secure File Downloader']")       # Page header text


    def secureFileDownload_LinkText(self):
        return self.driver.find_element(*SecureFileDownloadPage.secure_Link)

    def secureFileDownload_HeaderText(self):
        return self.driver.find_element(*SecureFileDownloadPage.secure_Header)


