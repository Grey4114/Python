"""
Website:  https://the-internet.herokuapp.com/nested_frames
Created:  2/16/2021
Notes:
    Connected Page Object Script - /pageObjects/NestedFramesPage.py
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.NestedFramesPage import NestedFramesPage


class TestNestedFrames(BaseClass):
    def test_Nested_frames(self):
        # Enter the Page
        driver = self.driver
        log = self.getLogger()
        nestedFrames_page = NestedFramesPage(self.driver)
        nestedFrames_page.nestedFrames_LinkText().click()


        # Verify the Header - No actual header text on this page
        log.info("Nested Frames")


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/nested_frames"
        log.info("URL: " + url)


        # Verify left frame
        self.driver.refresh()
        # NOTE - to get to the left, middle and right frames must go through the top frame first
        self.driver.switch_to.frame('frame-top')
        self.driver.switch_to.frame('frame-left')
        left = nestedFrames_page.nestedFrames_BodyText().text
        assert left == 'LEFT'


        # Verify middle frame
        self.driver.refresh()
        self.driver.switch_to.frame('frame-top')
        self.driver.switch_to.frame('frame-middle')
        middle = nestedFrames_page.nestedFrames_BodyText().text
        assert middle == 'MIDDLE'


        # Verify right frame
        self.driver.refresh()
        self.driver.switch_to.frame('frame-top')
        self.driver.switch_to.frame('frame-right')
        right = nestedFrames_page.nestedFrames_BodyText().text
        assert right == 'RIGHT'


        # Verify bottom frame
        self.driver.refresh()
        driver.switch_to.frame('frame-bottom')
        bottom = nestedFrames_page.nestedFrames_BodyText().text
        assert bottom == 'BOTTOM'


        # Exit the Page
        log.info("Nested Frames - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

