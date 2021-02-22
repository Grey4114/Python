"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HoversPage import HoversPage

class TestHovers(BaseClass):
    def test_hovers(self):
        # Enter the Page
        log = self.getLogger()
        hover_page = HoversPage(self.driver)
        log.info("TEST START")
        hover_page.hovers_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/hovers"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = hover_page.hovers_HeaderText().text
        assert ("Hovers" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify image & info 1
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify image & info 2
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify image & info 3
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



