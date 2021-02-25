"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.FileUploadPage import FileUploadPage


class TestFileUpload(BaseClass):

    def test_file_upload(self):
        # Enter the Page
        log = self.getLogger()
        fileUpload_page = FileUploadPage(self.driver)
        log.info("TEST START")
        fileUpload_page.fileUpload_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/upload"
        log.info("URL: " + url)


        # Verify the Header
        header_text = fileUpload_page.fileUpload_HeaderText().text
        assert ("File Uploader" in header_text)
        log.info("Header: " + header_text)


        # Choose a file and Upload
        fileUpload_page.fileUpload_ChooseFile().click()
        # todo - MSWindow - change dir, select file and select ok
        fileUpload_page.fileUpload_UploadButton().click()
        uploadtext = fileUpload_page.fileUpload_UploadedText().text
        fileUpload_page.fileUpload_FileUpload()     # todo - verify the file uploaded, not sure how to handle

        # todo - Verify drag and drop file into upload area
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



