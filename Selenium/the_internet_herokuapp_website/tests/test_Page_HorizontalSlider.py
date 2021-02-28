"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from selenium.webdriver import ActionChains

from utilities.BaseClass import BaseClass
from pageObjects.HorizontalSliderPage import HorizontalSliderPage

class TestHorizontalSlider(BaseClass):

    def test_horizontal_slider(self):
        # Enter the Page
        log = self.getLogger()
        horizontalSlider_page = HorizontalSliderPage(self.driver)
        log.info("TEST START")
        horizontalSlider_page.horizontalSlider_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/horizontal_slider"
        log.info("URL: " + url)

        # Verify the Header
        header_text = horizontalSlider_page.horizontalSlider_HeaderText().text
        assert ("Horizontal Slider" in header_text)
        log.info("Header: " + header_text)


        # Verify slider move
        assert horizontalSlider_page.horizontalSlider_SliderValue().text == "0"
        slider = horizontalSlider_page.horizontalSlider_Slider()
        ActionChains(self.driver).drag_and_drop_by_offset(slider, 0, 5).perform()
        assert horizontalSlider_page.horizontalSlider_SliderValue().text == "2.5"
        log.info("Moved: " + horizontalSlider_page.horizontalSlider_SliderValue().text)



        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




