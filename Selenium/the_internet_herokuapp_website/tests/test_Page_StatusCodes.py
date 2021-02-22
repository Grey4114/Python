"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.StatusCodesPage import StatusCodesPage

class TestStatusCodes(BaseClass):

    def test_status_codes(self):
        # Enter the Page
        log = self.getLogger()
        statusCodes_page = StatusCodesPage(self.driver)
        log.info("TEST START")
        statusCodes_page.statusCodes_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/status_codes"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = statusCodes_page.statusCodes_HeaderText().text
        assert ("Status Codes" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify 200
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify 301
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify 404
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify 500
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



