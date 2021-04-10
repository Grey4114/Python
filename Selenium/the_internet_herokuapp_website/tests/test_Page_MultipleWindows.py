"""
Website:  https://the-internet.herokuapp.com/windows
Created:  2/16/2021
Notes:
    Connected Page Object Script - /pageObjects/MultipleWindowsPage.py
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.MultipleWindowsPage import MultipleWindowsPage

class TestMultipleWindows(BaseClass):
    def test_multiple_windows(self):
        # Enter the Page
        log = self.getLogger()
        multipleWindows_page = MultipleWindowsPage(self.driver)
        multipleWindows_page.multipleWindows_LinkText().click()


        # Verify the Header
        header_text = multipleWindows_page.multipleWindows_HeaderText().text
        assert ("Opening a new window" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/windows"
        log.info("URL: " + url)


        # Verify open new window
        multipleWindows_page.multipleWindows_ClickHere().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert multipleWindows_page.multipleWindows_NewHeader().text == 'New Window'
        log.info(multipleWindows_page.multipleWindows_NewHeader().text)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

