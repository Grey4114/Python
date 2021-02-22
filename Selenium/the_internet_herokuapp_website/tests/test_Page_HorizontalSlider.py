"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HorizontalSliderPage import HorizontalSliderPage

class TestHorizontalSlider(BaseClass):

    def test_horizontal_slider(self):
        # Enter the Page
        log = self.getLogger()
        horizontalSlider_page = HorizontalSliderPage(self.driver)
        log.info("TEST START")
        horizontalSlider_page.horizontalSlider_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/horizontal_slider"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = horizontalSlider_page.horizontalSlider_HeaderText().text
        assert ("Horizontal Slider" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify slider 0
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify slider 3
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify slider 5
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




