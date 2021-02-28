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
        geolocation_page.geolocation_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/geolocation"
        log.info("URL: " + url)

        # Verify the Header
        header_text = geolocation_page.geolocation_HeaderText().text
        assert ("Geolocation" in header_text)
        log.info("Header: " + header_text)


        # Verify button, latitiude and longtitude
        geolocation_page.geolocation_WhereAmI_Button().click()
        time.sleep(3)
        assert "37" in geolocation_page.geolocation_LatitudeText().text
        assert "-121" in geolocation_page.geolocation_LongtitudeText().text
        log.info("Location: Passed")

        # Verify google link and page
        time.sleep(3)
        geolocation_page.geolocation_GoogleLink().click()
        time.sleep(3)
        assert "37" in geolocation_page.geolocation_GooglePage().text
        log.info("Goolge Page: Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



