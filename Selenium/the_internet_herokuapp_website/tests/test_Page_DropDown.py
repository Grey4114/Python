"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.DropDownPage import DropDownPage


class TestDropdown(BaseClass):

    def test_dropdown(self):
        # Enter the Page
        log = self.getLogger()
        dropdown_page = DropDownPage(self.driver)
        log.info("TEST START")
        dropdown_page.dropDown_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/dropdown"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = dropdown_page.dropDown_HeaderText().text
        assert ("Dropdown List" in header_text)
        log.info("Header Passed: " + header_text)


        # todo - Verify List no option
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify List option 1
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify List option 2
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



