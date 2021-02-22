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
        fileUpload_page.fileUpload_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/upload"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = fileUpload_page.fileUpload_HeaderText().text
        assert ("File Uploader" in header_text)
        log.info("Header Passed: " + header_text)


        # todo - Verify choose a file and upload
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

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



