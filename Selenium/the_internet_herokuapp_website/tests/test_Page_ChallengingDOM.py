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



        # Verify Blue, Red and Green Button id numbers change after clickin on one of the buttons
        # Grab the id numbers prior to button click
        blue_before = challenging_dom_page.challenging_ButtonBlue().get_attribute("id")
        red_before = challenging_dom_page.challenging_ButtonRed().get_attribute("id")
        green_before = challenging_dom_page.challenging_ButtonGreen().get_attribute("id")
        challenging_dom_page.challenging_ButtonBlue().click()

        # Grab the id numbers after to button click
        blue_after = challenging_dom_page.challenging_ButtonBlue().get_attribute("id")
        red_after = challenging_dom_page.challenging_ButtonRed().get_attribute("id")
        green_after = challenging_dom_page.challenging_ButtonGreen().get_attribute("id")

        # Logging the before and after id numbers for each button
        log.info("Blue Button: " + blue_before + " - " + blue_after)
        log.info("Red Button: " + red_before + " - " + red_after)
        log.info("Green Button: " + green_before + " - " + green_after)

        # Verify that the id #'s have changed
        assert blue_before != blue_after
        assert red_before != red_after
        assert green_before != green_after


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        # time.sleep(2)
        self.driver.back()
        self.driver.refresh()


