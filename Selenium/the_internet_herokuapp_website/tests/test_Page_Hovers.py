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
from pageObjects.HoversPage import HoversPage

# Todo - Hover is working on images, but unsure how to test that the hover text is shown

class TestHovers(BaseClass):
    def test_hovers(self):
        # Enter the Page
        log = self.getLogger()
        hover_page = HoversPage(self.driver)
        log.info("TEST START")
        hover_page.hovers_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/hovers"
        log.info("URL: " + url)


        # Verify the Header
        header_text = hover_page.hovers_HeaderText().text
        assert ("Hovers" in header_text)
        log.info("Header: " + header_text)


        # Select & Verify image & info 1
        action = ActionChains(self.driver)
        image1 = hover_page.hovers_Picture_1()
        action.move_to_element(image1).perform()
        time.sleep(3)
        # assert image1.text == 'name: user1'


        # Select & Verify image & info 2
        action = ActionChains(self.driver)
        image2 = hover_page.hovers_Picture_2()
        action.move_to_element(image2).perform()
        time.sleep(3)
        # assert image2.text == 'name: user1'


        # Select & Verify image & info 3
        action = ActionChains(self.driver)
        image3 = hover_page.hovers_Picture_3()
        action.move_to_element(image3).perform()
        time.sleep(3)
        # assert image3.text == 'name: user1'


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



