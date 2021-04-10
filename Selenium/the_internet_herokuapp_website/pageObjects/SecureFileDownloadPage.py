"""
Website:  https://the-internet.herokuapp.com/download_secure
Created:  2/15/2021
Notes:
    Connected Test Object Script - /tests/test_Page_SecureFileDownload.py

    - user and pass: admin
    - No page header text
    - Apparently there is only one way to test this type of pop-up Auth window
    - According to the internet there is no way to test cancel button or false user/pass for the pop-up Auth window

    ** Basic Auth & Digest Auth pages have the same issues as this page
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


