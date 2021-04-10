"""
Website:  https://the-internet.herokuapp.com/large
Created:  2/16/2021
Notes:
    Connected Page Object Script - /pageObjects/LargeDeepDOMPage.py
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.LargeDeepDOMPage import LargeDeepDOMPage

class TestLargeDeepDOM(BaseClass):
    def test_large_deep_dom(self):
        # Enter the Page
        log = self.getLogger()
        largeDeepDOM_page = LargeDeepDOMPage(self.driver)
        largeDeepDOM_page.largeDeepDOM_LinkText().click()


        # Verify the Header
        header_text = largeDeepDOM_page.largeDeepDOM_HeaderText().text
        assert ("Large & Deep DOM" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/large"
        log.info("URL: " + url)


        # Move to down location
        element = largeDeepDOM_page.largeDeepDOM_DownLocation()
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', element)
        assert element.text == '26.2'


        # Move to table location
        element2 = largeDeepDOM_page.largeDeepDOM_TableLocation()
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', element2)
        assert element2.text == '15.25'


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

