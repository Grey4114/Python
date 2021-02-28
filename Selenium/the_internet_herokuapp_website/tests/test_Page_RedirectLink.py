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
        redirectLink_page.redirectLink_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/redirector"
        log.info("URL: " + url)


        # Verify the Header
        header_text = redirectLink_page.redirectLink_HeaderText().text
        assert ("Redirection" in header_text)
        log.info("Header: " + header_text)


        # Verify new page url
        redirectLink_page.redirectLink_ClickHere().click()
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/status_codes"
        log.info("Redirected: " + url)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



