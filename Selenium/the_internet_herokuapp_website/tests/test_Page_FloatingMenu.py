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
        time.sleep(3)
        page = floatingMenu_page.floatingMenu_PageInfo()
        # floatingMenu_page.floatingMenu_HomeButton()     # todo - check position
        # floatingMenu_page.floatingMenu_NewsButton()     # todo - check position
        # floatingMenu_page.floatingMenu_ContactButton()  # todo - check position
        # floatingMenu_page.floatingMenu_AboutButton()    # todo - check position

        page.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)


        # todo - Verify - Scroll down and check menu Postion
        # floatingMenu_page.floatingMenu_Scroll()
        # floatingMenu_page.floatingMenu_HomeButton()
        # floatingMenu_page.floatingMenu_NewsButton()
        # floatingMenu_page.floatingMenu_ContactButton()
        # floatingMenu_page.floatingMenu_AboutButton()

        # assert (xXxX in xxxx)             # todo
        # log.info("Elements Passed")       # todo



        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




