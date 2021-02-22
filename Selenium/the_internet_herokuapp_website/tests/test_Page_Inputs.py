"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.InputsPage import InputsPage

class TestInputs(BaseClass):

    def test_inputs(self):
        # Enter the Page
        log = self.getLogger()
        inputs_page = InputsPage(self.driver)
        log.info("TEST START")
        inputs_page.inputs_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/inputs"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = inputs_page.inputs_HeaderText().text
        assert ("Inputs" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify manual
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify arrow input
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



