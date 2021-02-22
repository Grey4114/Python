"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.GeolocationPage import GeolocationPage

class TestGeolocation(BaseClass):
    def test_geolocation(self):
        # Enter the Page
        log = self.getLogger()
        geolocation_page = GeolocationPage(self.driver)
        log.info("TEST START")
        geolocation_page.geolocation_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/geolocation"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = geolocation_page.geolocation_HeaderText().text
        assert ("Geolocation" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify button
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify latitiude
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify longtitude
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify google link
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



