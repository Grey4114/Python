"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.InfiniteScrollPage import InfiniteScrollPage

class TestInfiniteScroll(BaseClass):

    def test_infinite_scroll(self):

        # Enter the Page
        log = self.getLogger()
        infiniteScroll_page = InfiniteScrollPage(self.driver)
        log.info("TEST START")
        infiniteScroll_page.infiniteScroll_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/infinite_scroll"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = infiniteScroll_page.infiniteScroll_HeaderText().text
        assert ("Infinite Scroll" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify scroll 1
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify scroll 2
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




