"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intentpage
"""

from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - File Download


class FileDownloadPage:
    def __init__(self, driver):
        self.driver = driver

    download_LinkText = (By.XPATH, "//a[text()='File Download']")

    def fileDownload_Link(self):
        return self.driver.find_element(*FileDownloadPage.download_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='File Download']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """
