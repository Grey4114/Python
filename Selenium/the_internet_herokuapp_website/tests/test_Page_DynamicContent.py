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

    def test_dynamic_content(self):
        # Enter the Page
        log = self.getLogger()
        dynamicContent_page = DynamicContentPage(self.driver)
        log.info("TEST START")
        dynamicContent_page.dynamicContent_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/dynamic_content?with_content=static"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = dynamicContent_page.dynamicContent_HeaderText().text
        assert ("Dynamic Content" in header_text)
        log.info("Header Passed: " + header_text)



        # todo - Verify image & text 1
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify image & text 2
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify image & text 3 A-C
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")



        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



