"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.FloatingMenuPage import FloatingMenuPage

class TestFloatingMenu(BaseClass):

    def test_floating_menu(self):
        # Enter the Page
        log = self.getLogger()
        floatingMenu_page = FloatingMenuPage(self.driver)
        log.info("TEST START")
        floatingMenu_page.floatingMenu_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/floating_menu"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = floatingMenu_page.floatingMenu_HeaderText().text
        assert ("Floating Menu" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify menu slider
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




