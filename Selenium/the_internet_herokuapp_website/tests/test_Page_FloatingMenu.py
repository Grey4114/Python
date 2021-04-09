"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
        log.info("URL: " + url)


        # Verify the Header
        header_text = floatingMenu_page.floatingMenu_HeaderText().text
        assert ("Floating Menu" in header_text)
        log.info("Header: " + header_text)


        # Floating menu - check position - Home, News, Contact & About
        before = floatingMenu_page.floatingMenu_PageMenu().location
        # log.info(before['y'])
        floatingMenu_page.floatingMenu_PageBody().send_keys(Keys.PAGE_DOWN)
        after = floatingMenu_page.floatingMenu_PageMenu().location
        # log.info(after['y'])
        assert before['y'] != after['y']


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




