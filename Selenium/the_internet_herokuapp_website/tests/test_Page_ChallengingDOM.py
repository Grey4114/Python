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

# todo - Verify Blue Button
# todo - Verify Red Button
# todo - Verify Green Button
# todo - Verify Answer Change


class TestChallengingDOM(BaseClass):

    def test_challenging_dom(self):
        # Enter the Page
        log = self.getLogger()
        challenging_dom_page = ChallengingDomPage(self.driver)
        log.info("TEST PAGE: Challenging DOM")
        challenging_dom_page.challengingDom_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/challenging_dom"
        log.info("URL - Passed: " + url)


        # Verify the Header
        header_text = challenging_dom_page.challengingDom_HeaderText().text
        assert ("Challenging DOM" in header_text)
        log.info("Header - Passed: " + header_text)


        # Verify Blue Button
        # add_remove_page.addElement().click()
        # assert len(add_remove_page.delElements())
        # log.info("Add Buttons - Passed")


        # Verify Red Button
        # add_remove_page.addElement().click()
        # assert len(add_remove_page.delElements())
        # log.info("Add Buttons - Passed")


        # Verify Green Button
        # add_remove_page.addElement().click()
        # assert len(add_remove_page.delElements())
        # log.info("Add Buttons - Passed")


        # Verify Answer Change
        # add_remove_page.addElement().click()
        # assert len(add_remove_page.delElements())
        # log.info("Add Buttons - Passed")



        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


