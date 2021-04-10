"""
Website:  https://the-internet.herokuapp.com/key_presses
Created:  2/16/2021
Notes:
    Connected Page Object Script - /pageObjects/KeyPressesPage.py
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
        keyPresses_page.keyPresses_LinkText().click()


        # Verify the Header
        header_text = keyPresses_page.keyPresses_HeaderText().text
        assert ("Key Presses" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/key_presses"
        log.info("URL: " + url)


        # Verify field & text: number
        keyPresses_page.keyPresses_Field().send_keys("7")
        assert keyPresses_page.keyPresses_Text().text == "You entered: 7"
        # log.info(keyPresses_page.keyPresses_Text().text)


        # Verify Verify field & text: letter
        keyPresses_page.keyPresses_Field().send_keys("q")
        assert keyPresses_page.keyPresses_Text().text == "You entered: Q"
        # log.info(keyPresses_page.keyPresses_Text().text)


        # Verify Verify field & text: character
        keyPresses_page.keyPresses_Field().send_keys("/")
        assert keyPresses_page.keyPresses_Text().text == "You entered: SLASH"
        # log.info(keyPresses_page.keyPresses_Text().text)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


