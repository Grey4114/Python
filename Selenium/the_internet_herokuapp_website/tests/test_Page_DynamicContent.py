"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.DynamicContentPage import DynamicContentPage


class TestDynamicContent(BaseClass):

    # image_1 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-1.jpg"
    # image_2 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-2.jpg"
    # image_3 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg"
    # image_4 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-5.jpg"
    # image_5 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-7.jpg"

    def test_dynamic_content(self):
        # Enter the Page
        log = self.getLogger()
        dynamicContent_page = DynamicContentPage(self.driver)
        log.info("TEST START")
        dynamicContent_page.dynamicContent_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/dynamic_content"
        log.info("URL: " + url)


        # Verify the Header
        header_text = dynamicContent_page.dynamicContent_HeaderText().text
        assert ("Dynamic Content" in header_text)
        log.info("Header: " + header_text)


        # Images Before click
        images_before = dynamicContent_page.dynamicContent_PageImages()
        before_I0 = images_before[0].get_attribute("src")
        before_I1 = images_before[1].get_attribute("src")
        before_I2 = images_before[2].get_attribute("src")


        # Text - Before click
        texts_before = dynamicContent_page.dynamicContent_PageTexts()
        before_T0 = texts_before[0].text
        before_T1 = texts_before[1].text
        before_T2 = texts_before[2].text


        # Refresh the page
        time.sleep(5)
        dynamicContent_page.dynamicContent_ClickHere().click()
        time.sleep(2)


        # Images After click
        images_after = dynamicContent_page.dynamicContent_PageImages()
        after_I0 = images_after[0].get_attribute("src")
        after_I1 = images_after[1].get_attribute("src")
        after_I2 = images_after[2].get_attribute("src")


        # Text After click
        texts_after = dynamicContent_page.dynamicContent_PageTexts()
        after_T0 = texts_after[0].text
        after_T1 = texts_after[1].text
        after_T2 = texts_after[2].text


        # Verify images
        assert before_I0 != after_I0
        assert before_I1 != after_I1
        assert before_I2 != after_I2
        log.info("Images: Passed")

        # Verify text
        assert before_T0 != after_T0
        assert before_T1 != after_T1
        assert before_T2 != after_T2
        log.info("Texts: Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

