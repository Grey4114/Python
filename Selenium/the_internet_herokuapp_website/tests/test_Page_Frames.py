"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.FramesPage import FramesPage

class TestFrames(BaseClass):

    def test_frames(self):
        # Enter the Page
        log = self.getLogger()
        frames_page = FramesPage(self.driver)
        log.info("TEST START")
        frames_page.frames_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/frames"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = frames_page.frames_HeaderText().text
        assert ("Frames" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify nested page
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify nested right
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify nested left
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify nested bottom
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify iframe page
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify iframe area
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify iframe - all other options


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




