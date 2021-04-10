"""
Website:  https://the-internet.herokuapp.com/broken_images
Created:  2/9/2021
Notes:
    Connected Page Object Script - /pageObjects/BrokenImagesPage.py
"""

import time
import pytest
from pip._vendor import requests

from utilities.BaseClass import BaseClass
from pageObjects.BrokenImagesPage import BrokenImagePage

class TestBrokenImages(BaseClass):

    def test_broken_images(self):
        # Enter the Page
        log = self.getLogger()
        broken_image_page = BrokenImagePage(self.driver)
        broken_image_page.broken_LinkText().click()


        # Verify the Header
        header_text = broken_image_page.broken_HeaderText().text
        assert ("Broken Images" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/broken_images"
        log.info("URL: " + url)

        # Find Broken Images
        image_list = broken_image_page.brokenImage_List()
        # iBrokenImageCount = 0
        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if (response.status_code != 200):
                    assert img.get_attribute('outerHTML') == '<img src="asdf.jpg">' or \
                           img.get_attribute('outerHTML') == '<img src="hjkl.jpg">'
                    # print(img.get_attribute('outerHTML') + " is broken.")
                    log.info(img.get_attribute('outerHTML') + " is broken.")

            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except:
                print("Encountered Some other Exception")



        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


