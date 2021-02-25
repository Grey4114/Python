"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.BrokenImagesPage import BrokenImagePage

class TestBrokenImages(BaseClass):

    def test_broken_images(self):
        # Enter the Page
        log = self.getLogger()
        broken_image_page = BrokenImagePage(self.driver)
        log.info("TEST START")
        broken_image_page.broken_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/broken_images"
        log.info("URL: " + url)


        # Verify the Header
        header_text = broken_image_page.broken_HeaderText().text
        assert ("Broken Images" in header_text)
        log.info("Header: " + header_text)


        # todo - Verify Image 1
        # size1 = broken_image_page.brokenImage_1()
        # assert broken_image_page.brokenImage_1().is_displayed()
        # log.info("Image 1 - Passed")


        # todo - Verify Image 2
        # broken_image_page.brokenImage_2()
        # assert len(add_remove_page.delElements())
        # log.info("Add Buttons - Passed")


        # todo - Verify Image 2
        # broken_image_page.brokenImage_3()
        # assert len(add_remove_page.delElements())
        # log.info("Add Buttons - Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


