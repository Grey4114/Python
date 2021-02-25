"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.ChallengingDomPage import ChallengingDomPage

class TestChallengingDOM(BaseClass):

    def test_challenging_dom(self):
        # Enter the Page
        log = self.getLogger()
        challenging_dom_page = ChallengingDomPage(self.driver)
        log.info("TEST START")
        challenging_dom_page.challengingDom_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/challenging_dom"
        log.info("URL: " + url)


        # Verify the Header
        header_text = challenging_dom_page.challengingDom_HeaderText().text
        assert ("Challenging DOM" in header_text)
        log.info("Header: " + header_text)


        # todo - Verify Blue Button
        before = challenging_dom_page.challenging_ButtonBlue().text
        challenging_dom_page.challenging_ButtonBlue().click()
        after = challenging_dom_page.challenging_ButtonBlue().text
        assert before != after
        log.info("Blue Button: " + before + "-" + after)


        # todo - Verify Red Button
        before = challenging_dom_page.challenging_ButtonRed().text
        challenging_dom_page.challenging_ButtonRed().click()
        after = challenging_dom_page.challenging_ButtonRed().text
        assert before != after
        log.info("Red Button: " + before + "-" + after)


        # todo - Verify Green Button
        before = challenging_dom_page.challenging_ButtonGreen().text
        challenging_dom_page.challenging_ButtonGreen().click()
        after = challenging_dom_page.challenging_ButtonGreen().text
        assert before != after
        log.info("Blue Button: " + before + "-" + after)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        # time.sleep(2)
        self.driver.back()
        self.driver.refresh()


