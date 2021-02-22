"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the A/B Test page using the abPage objects script

"""

import time
import pytest
from selenium.common.exceptions import NoSuchElementException

from utilities.BaseClass import BaseClass
from pageObjects.abPage import abPage


class TestAB(BaseClass):
    def test_ab_control(self):
        # Enter the Page
        log = self.getLogger()
        ab_page = abPage(self.driver)
        ab_page.ab_Link().click()
        log.info("TEST PAGE: A/B Test")


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/abtest"
        log.info("URL - Passed: " + url)


        # Verify the Header
        try:
            header_text = ab_page.ab_HeaderText_1().text
        except NoSuchElementException:
            header_text = ab_page.ab_HeaderText_2().text

        assert ("A/B Test" in header_text)
        log.info("Header - Passed: " + header_text)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        # time.sleep(2)
        self.driver.back()
        self.driver.refresh()
