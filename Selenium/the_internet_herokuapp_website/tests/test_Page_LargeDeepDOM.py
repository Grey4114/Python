"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.LargeDeepDOMPage import LargeDeepDOMPage

class TestLargeDeepDOM(BaseClass):

    def test_large_deep_dom(self):
        # Enter the Page
        log = self.getLogger()
        largeDeepDOM_page = LargeDeepDOMPage(self.driver)
        log.info("TEST START")
        largeDeepDOM_page.largeDeepDOM_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/large"
        log.info("URL: " + url)

        # Verify the Header
        header_text = largeDeepDOM_page.largeDeepDOM_HeaderText().text
        assert ("Large & Deep DOM" in header_text)
        log.info("Header: " + header_text)


        # todo - not sure what to test for
        # todo - Verify scroll down
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # todo - Verify scroll across
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # todo - Verify text
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")



        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



