"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.ShadowDOMPage import ShadowDOMPage

class TestShadowDOM(BaseClass):

    def test_shadow_dom(self):
        # Enter the Page
        log = self.getLogger()
        shadowDOM_page = ShadowDOMPage(self.driver)
        log.info("TEST START")
        shadowDOM_page.shadowDOM_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/shadowdom"
        log.info("URL Passed: " + url)

        # todo - Verify the Header
        header_text = shadowDOM_page.shadowDOM_HeaderText().text
        assert ("Simple template" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify text 1
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify text 2
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


