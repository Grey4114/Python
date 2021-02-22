"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.TyposPage import TyposPage

class TestTypos(BaseClass):

    def test_typos(self):
        # Enter the Page
        log = self.getLogger()
        typos_page = TyposPage(self.driver)
        log.info("TEST START")
        typos_page.typos_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/typos"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = typos_page.typos_HeaderText().text
        assert ("Typos" in header_text)
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




