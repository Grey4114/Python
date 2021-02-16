"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intentpage
"""

from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - File Upload


class FileUploadPage:
    def __init__(self, driver):
        self.driver = driver

    upload_LinkText = (By.XPATH, "//a[text()='File Upload']")


    def fileUpload_Link(self):
        return self.driver.find_element(*FileUploadPage.upload_LinkText)



    """
    driver.find_element(By.XPATH, "//a[text()='File Upload']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """