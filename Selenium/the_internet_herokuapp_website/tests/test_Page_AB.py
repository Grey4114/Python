"""
Webpage:  https://the-internet.herokuapp.com/abtest
Created:  2/16/2021
Notes:
    Connected Page Object Script - /pageObjects/abPage.py
"""
import time
import pytest
from selenium.common.exceptions import NoSuchElementException

from utilities.BaseClass import BaseClass
from pageObjects.abPage import abPage


class TestPageAB(BaseClass):
    def test_ab_control(self):
        # Enter the Page
        log = self.getLogger()
        ab_page = abPage(self.driver)
        ab_page.ab_LinkText().click()

        # Verify the Header
        try:
            header_text = ab_page.ab_HeaderText_1().text
        except NoSuchElementException:
            header_text = ab_page.ab_HeaderText_2().text

        assert ("A/B Test" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/abtest"
        log.info("URL: " + url)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()
