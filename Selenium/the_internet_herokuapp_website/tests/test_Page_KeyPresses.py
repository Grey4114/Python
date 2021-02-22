"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.KeyPressesPage import KeyPressesPage

class TestKeyPresses(BaseClass):

    def test_key_presses(self):

        # Enter the Page
        log = self.getLogger()
        keyPresses_page = KeyPressesPage(self.driver)
        log.info("TEST START")
        keyPresses_page.keyPresses_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/key_presses"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = keyPresses_page.keyPresses_HeaderText().text
        assert ("Key Presses" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify field & text: number
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify Verify field & text: letter
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify Verify field & text: character
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


