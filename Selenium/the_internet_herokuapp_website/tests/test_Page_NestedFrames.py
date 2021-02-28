"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.NestedFramesPage import NestedFramesPage

class TestNestedFrames(BaseClass):

    def test_Nested_frames(self):
        # Enter the Page
        log = self.getLogger()
        nestedFrames_page = NestedFramesPage(self.driver)
        log.info("TEST START")
        nestedFrames_page.nestedFrames_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/nested_frames"
        log.info("URL: " + url)

        # Verify the Header
        header_text = nestedFrames_page.nestedFrames_HeaderText().text
        assert ("Xxxxx" in header_text)
        log.info("Header: " + header_text)

        # todo - not sure how to test this at this time

        # todo - Verify right frame
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify left frame
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify bottom frame
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



