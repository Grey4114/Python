"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.SlowResourcesPage import SlowResourcesPage

class TestSlowResources(BaseClass):

    def test_slow_resources(self):

        # Enter the Page
        log = self.getLogger()
        slowResources_page = SlowResourcesPage(self.driver)
        log.info("TEST START")
        slowResources_page.slowResources_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/slow"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = slowResources_page.slowResources_HeaderText().text
        assert ("Slow Resources" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify get request
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify get request
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




