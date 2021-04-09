"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This page simply links to 2 other pages that already have test scripts writtem for them
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
        frames_page.frames_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/frames"
        log.info("URL: " + url)

        # Verify the Header
        header_text = frames_page.frames_HeaderText().text
        assert ("Frames" in header_text)
        log.info("Header: " + header_text)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




