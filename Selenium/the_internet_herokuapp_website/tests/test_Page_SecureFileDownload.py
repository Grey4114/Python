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

class TestSecureFileDownload(BaseClass):

    def test_secure_file_download(self):

        # Enter the Page
        log = self.getLogger()
        secureFileDownload_page = SecureFileDownloadPage(self.driver)
        log.info("TEST START")
        secureFileDownload_page.secureFileDownload_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/download_secure"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = secureFileDownload_page.secureFileDownload_HeaderText().text
        assert ("Secure File Download" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify valid sign in
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify invalid sign in
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify cancel
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



