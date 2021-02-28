"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
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
        log.info("TEST START")
        shadowDOM_page.shadowDOM_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/shadowdom"
        log.info("URL: " + url)

        # todo - Verify the Header
        header_text = shadowDOM_page.shadowDOM_HeaderText().text
        assert ("Simple template" in header_text)
        log.info("Header: " + header_text)

        # todo - Verify text 1
        text1 = shadowDOM_page.shadowDOM_Text_1().text
        text2 = shadowDOM_page.shadowDOM_Text_2().text

        assert "Let's have some different text!" in text1
        assert "In a list!" in text2

        log.info("Text Elements Passed")



        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


