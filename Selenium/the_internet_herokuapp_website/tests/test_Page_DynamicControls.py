"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.DynamicControlsPage import DynamicControlsPage

class TestDynamicControls(BaseClass):

    def test_dynamic_controls(self):

        # Enter the Page
        log = self.getLogger()
        dynamicControls_page = DynamicControlsPage(self.driver)
        log.info("TEST START")
        dynamicControls_page.dynamicControls_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/dynamic_controls"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = dynamicControls_page.dynamicControls_HeaderText().text
        assert ("Dynamic Controls" in header_text)
        log.info("Header Passed: " + header_text)



        # todo - Verify remove checkbox & text
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify add checkbox & text
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify enable field & text
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify disable field & text
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



