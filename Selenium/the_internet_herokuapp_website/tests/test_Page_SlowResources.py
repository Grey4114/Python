"""
Website:  https://the-internet.herokuapp.com/slow
Created:  2/16/2021
Notes:
    Connected Page Object Script - pageObjects/SlowResourcesPage.py
"""

import time
import pytest
import requests
from utilities.BaseClass import BaseClass
from pageObjects.SlowResourcesPage import SlowResourcesPage

# TODO - Not sure how to verify GET request at this time

class TestSlowResources(BaseClass):
    def test_slow_resources(self):
        # Enter the Page
        log = self.getLogger()
        slowResources_page = SlowResourcesPage(self.driver)
        slowResources_page.slowResources_LinkText().click()


        # Verify the Header
        header_text = slowResources_page.slowResources_HeaderText().text
        assert ("Slow Resources" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/slow"
        log.info("URL: " + url)


        # Verify GET request
        # req = requests.get("https://the-internet.herokuapp.com/slow")
        # assert req.status_code == 200
        # log.info(req.status_code)
        # time.sleep(30)
        # self.driver.execute_script("$.get('/slow_external').click()")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




