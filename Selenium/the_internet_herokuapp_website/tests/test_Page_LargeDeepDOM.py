"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.LargeDeepDOMPage import LargeDeepDOMPage

class TestLargeDeepDOM(BaseClass):

    def test_large_deep_dom(self):
        # Enter the Page
        log = self.getLogger()
        largeDeepDOM_page = LargeDeepDOMPage(self.driver)
        log.info("TEST START")
        largeDeepDOM_page.largeDeepDOM_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/large"
        log.info("URL: " + url)

        # Verify the Header
        header_text = largeDeepDOM_page.largeDeepDOM_HeaderText().text
        assert ("Large & Deep DOM" in header_text)
        log.info("Header: " + header_text)



        # Move to down location
        # time.sleep(2)
        element = largeDeepDOM_page.largeDeepDOM_DownLocation()
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', element)
        # loc = element.location
        # log.info(loc)
        # time.sleep(2)
        assert element.text == '26.2'



        # Move to table location
        # time.sleep(2)
        element2 = largeDeepDOM_page.largeDeepDOM_TableLocation()
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', element2)
        # loc = element2.location
        # log.info(loc)
        # time.sleep(2)
        assert element2.text == '15.25'




        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



