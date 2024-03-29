"""
Website:  https://the-internet.herokuapp.com/upload
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_FileUpload.py
"""

from selenium.webdriver.common.by import By

class FileUploadPage:
    def __init__(self, driver):
        self.driver = driver

    upload_Link = (By.XPATH, "//a[text()='File Upload']")                       # Main Page link
    upload_Header = (By.XPATH, "//h3[text()='File Uploader']")                  # Page header text

    upload_Choose = (By.CSS_SELECTOR, "#file-upload")                   # Choose button
    upload_Upload = (By.XPATH, "//input[@class='button']")              # Upload button
    upload_DragDrop = (By.CSS_SELECTOR, "#drag-drop-upload")            # Drag drop box
    upload_Uploaded = (By.XPATH, "//h3[text()='File Uploaded!']")       # File uploaded text
    upload_File = (By.XPATH, "//div[@id='uploaded-files']")             # File uploaded text


    def fileUpload_LinkText(self):
        return self.driver.find_element(*FileUploadPage.upload_Link)

    def fileUpload_HeaderText(self):
        return self.driver.find_element(*FileUploadPage.upload_Header)

    def fileUpload_ChooseFile(self):
        return self.driver.find_element(*FileUploadPage.upload_Choose)

    def fileUpload_UploadButton(self):
        return self.driver.find_element(*FileUploadPage.upload_Upload)

    def fileUpload_DragDropArea(self):
        return self.driver.find_element(*FileUploadPage.upload_DragDrop)

    def fileUpload_UploadedText(self):
        return self.driver.find_element(*FileUploadPage.upload_Uploaded)

    def fileUpload_UploadedFile(self):
        return self.driver.find_element(*FileUploadPage.upload_File)

