"""
Website:  https://the-internet.herokuapp.com/shadowdom
Created:  2/16/2021
Notes:
    Connected Page Object Script - /pageObjects/ShadowDOMPage.py
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.ShadowDOMPage import ShadowDOMPage

class TestShadowDOM(BaseClass):
    def test_shadow_dom(self):
        # Enter the Page
        log = self.getLogger()
        shadowDOM_page = ShadowDOMPage(self.driver)
        shadowDOM_page.shadowDOM_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/shadowdom"
        log.info("URL: " + url)

        # Verify the Header
        header_text = shadowDOM_page.shadowDOM_HeaderText().text
        assert ("Simple template" in header_text)
        log.info("Header: " + header_text)

        # Verify the text
        text1 = shadowDOM_page.shadowDOM_Text_1().text
        text2 = shadowDOM_page.shadowDOM_Text_2().text
        assert "Let's have some different text!" in text1
        assert "In a list!" in text2


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


