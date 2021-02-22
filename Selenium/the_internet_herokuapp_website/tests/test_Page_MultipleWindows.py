"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.MultipleWindowsPage import MultipleWindowsPage

class TestMultipleWindows(BaseClass):

    def test_multiple_windows(self):
        # Enter the Page
        log = self.getLogger()
        multipleWindows_page = MultipleWindowsPage(self.driver)
        log.info("TEST START")
        multipleWindows_page.multipleWindows_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/windows"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = multipleWindows_page.multipleWindows_HeaderText().text
        assert ("Open a new window" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify opem new window part 1
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify opem new window part 2
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

