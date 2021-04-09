"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.SecureFileDownloadPage import SecureFileDownloadPage

# NOTE - user and pass: admin
# NOTE - Apparently there is only one way to test this type of pop-up Auth window
# NOTE - According to the internet there is no way to test cancel button

class TestSecureFileDownload(BaseClass):

    def test_secure_file_download(self):
        # Enter the Page
        log = self.getLogger()
        secureFileDownload_page = SecureFileDownloadPage(self.driver)
        log.info("TEST START")
        secureFileDownload_page.secureFileDownload_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/download_secure"
        log.info("URL: " + url)


        # Info info in pop up
        time.sleep(2)
        self.driver.get('https://admin:admin@the-internet.herokuapp.com/download_secure')


        # Verify the Header
        header_text = secureFileDownload_page.secureFileDownload_HeaderText().text
        assert ("Secure File Downloader" in header_text)
        log.info("Header: " + header_text)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



