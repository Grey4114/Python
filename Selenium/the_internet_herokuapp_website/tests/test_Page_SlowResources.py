"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    Connected Web Page Info - pageObjects/SlowResourcesPage.py
"""

import time
import pytest
import requests

from utilities.BaseClass import BaseClass
from pageObjects.SlowResourcesPage import SlowResourcesPage

class TestSlowResources(BaseClass):
    def test_slow_resources(self):

        # Enter the Page
        log = self.getLogger()
        slowResources_page = SlowResourcesPage(self.driver)
        log.info("TEST START")
        slowResources_page.slowResources_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/slow"
        log.info("URL: " + url)

        # Verify the Header
        header_text = slowResources_page.slowResources_HeaderText().text
        assert ("Slow Resources" in header_text)
        log.info("Header: " + header_text)


        # Todo - not sure how to verify GET request at this time
        # Verify GET request
        req = requests.get("https://the-internet.herokuapp.com/slow")
        # assert req.status_code == 200
        log.info(req.status_code)
        time.sleep(30)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




