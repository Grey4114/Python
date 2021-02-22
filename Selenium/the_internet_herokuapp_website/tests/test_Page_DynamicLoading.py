"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.DynamicLoadingPage import DynamicLoadingPage

class TestDynamicLoading(BaseClass):

    def test_dynamic_loading(self):
        # Enter the Page
        log = self.getLogger()
        dynamicLoading_page = DynamicLoadingPage(self.driver)
        log.info("TEST START")
        dynamicLoading_page.dynamicLoading_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/dynamic_loading"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = dynamicLoading_page.dynamicLoading_HeaderText().text
        assert ("Dynamically Loaded Page Elements" in header_text)
        log.info("Header Passed: " + header_text)


        # todo - Verify example 1
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify example 2
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



