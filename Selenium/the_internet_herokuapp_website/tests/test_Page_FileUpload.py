"""
Website:  https://the-internet.herokuapp.com/upload
Created:  2/9/2021
Notes:
    Connected Page Object Script - /pageObjects/FileUploadPage.py

    - Unable to drop get a file into the drag&drop area
    - Could not find an internet site that explained how to make the drag&drop file area work with selenium
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.FileUploadPage import FileUploadPage

# TODO - Learn how to get drag&drop file area to work

class TestFileUpload(BaseClass):
    def test_file_upload(self):
        # Enter the Page
        log = self.getLogger()
        fileUpload_page = FileUploadPage(self.driver)
        fileUpload_page.fileUpload_LinkText().click()


        # Verify the Header
        header_text = fileUpload_page.fileUpload_HeaderText().text
        assert ("File Uploader" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/upload"
        log.info("URL: " + url)


        # Verify - Choose a file and Upload
        button = fileUpload_page.fileUpload_ChooseFile()
        button.send_keys("D:/GitHub/Python/Selenium/the_internet_herokuapp_website/testData/test_upload.txt")
        fileUpload_page.fileUpload_UploadButton().click()
        time.sleep(3)
        assert fileUpload_page.fileUpload_UploadedText().text == "File Uploaded!"
        assert fileUpload_page.fileUpload_UploadedFile().text == "test_upload.txt"
        self.driver.back()
        self.driver.refresh()
        time.sleep(3)


        # Verify drag and drop file into upload area
        # dragdrop = fileUpload_page.fileUpload_DragDropArea()
        # dragdrop.send_keys("D:/GitHub/Python/Selenium/the_internet_herokuapp_website/testData/test_upload_DD.txt")
        # time.sleep(3)
        # fileUpload_page.fileUpload_UploadButton().click()
        # time.sleep(3)
        # assert fileUpload_page.fileUpload_UploadedText().text == "File Uploaded!"
        # assert fileUpload_page.fileUpload_UploadedFile().text == "test_upload_DD.txt"


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



