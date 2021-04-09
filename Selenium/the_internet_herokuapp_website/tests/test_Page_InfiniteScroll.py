"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from utilities.BaseClass import BaseClass
from pageObjects.InfiniteScrollPage import InfiniteScrollPage


class TestInfiniteScroll(BaseClass):
    def test_infinite_scroll(self):
        # Enter the Page
        log = self.getLogger()
        infiniteScroll_page = InfiniteScrollPage(self.driver)
        log.info("TEST START")
        infiniteScroll_page.infiniteScroll_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/infinite_scroll"
        log.info("URL: " + url)

        # Verify the Header
        header_text = infiniteScroll_page.infiniteScroll_HeaderText().text
        assert ("Infinite Scroll" in header_text)
        log.info("Header: " + header_text)

        # Verify scrolling down the page
        # Get current scroll height
        start_height = self.driver.execute_script("return document.body.scrollHeight")
        log.info(start_height)

        # Scroll down the page 20 times
        for x in range(1, 20):
            # Scroll down to bottom of the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(1)

            # Calculate new scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")

        log.info(new_height)

        # Check scroll height
        assert start_height != new_height


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(3)
        self.driver.back()
        self.driver.refresh()




