"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.EntryAdPage import EntryAdPage

class TestEntryAd(BaseClass):

    def test_entry_ad(self):
        # Enter the Page
        log = self.getLogger()
        entryad_page = EntryAdPage(self.driver)
        log.info("TEST START")
        entryad_page.entry_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/entry_ad"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = entryad_page.entry_Header().text
        assert ("Entry Ad" in header_text)
        log.info("Header Passed: " + header_text)


        # todo - Verify window header text
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify window close
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify click here
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

