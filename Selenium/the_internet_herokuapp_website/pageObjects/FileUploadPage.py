"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intentpage
"""

from selenium.webdriver.common.by import By


class FileUploadPage:
    def __init__(self, driver):
        self.driver = driver

    upload_LinkText = (By.XPATH, "//a[text()='File Upload']")
    upload_Header = (By.XPATH, "//h3[text()='File Uploader']")

    # todo - choose path
    upload_Choose = (By.XPATH, "")
    # todo - upload path
    upload_Upload = (By.XPATH, "")
    # todo - drag drop path
    upload_DragDrop = (By.XPATH, "")


    def fileUpload_Link(self):
        return self.driver.find_element(*FileUploadPage.upload_LinkText)

    def fileUpload_HeaderText(self):
        return self.driver.find_element(*FileUploadPage.upload_Header)

    def fileUpload_ChooseFile(self):
        return self.driver.find_element(*FileUploadPage.upload_Choose)

    def fileUpload_UploadButton(self):
        return self.driver.find_element(*FileUploadPage.upload_Upload)

    def fileUpload_DragDrop(self):
        return self.driver.find_element(*FileUploadPage.upload_DragDrop)

