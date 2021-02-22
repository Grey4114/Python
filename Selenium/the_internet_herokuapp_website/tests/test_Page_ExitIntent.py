"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.ExitIntentPage import ExitIntentPage

class TestExitIntent(BaseClass):

    def test_exit_intent(self):

        # Enter the Page
        log = self.getLogger()
        exitIntent_page = ExitIntentPage(self.driver)
        log.info("TEST START")
        exitIntent_page.exitIntent_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/exit_intent"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = exitIntent_page.exitIntent_HeaderText().text
        assert ("Exit Intent" in header_text)
        log.info("Header Passed: " + header_text)


        # todo - Verify mouse
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify window
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



