"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.RedirectLinkPage import RedirectLinkPage

class TestRedirectLink(BaseClass):

    def test_redirect_link(self):
        # Enter the Page
        log = self.getLogger()
        redirectLink_page = RedirectLinkPage(self.driver)
        log.info("TEST START")
        redirectLink_page.redirectLink_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/redirector"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = redirectLink_page.redirectLink_HeaderText().text
        assert ("Redirection" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify new page url
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify new page header
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



