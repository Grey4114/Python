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
        dropdown_page.dropDown_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/dropdown"
        log.info("URL: " + url)


        # Verify the Header
        header_text = dropdown_page.dropDown_HeaderText().text
        assert ("Dropdown List" in header_text)
        log.info("Header: " + header_text)


        # Verify List all options
        options = dropdown_page.dropDown_List()
        options_text = ["Please select an option", "Option 1", "Option 2"]
        count = 0

        for opt in options:
            opt.click()
            assert opt.text == options_text[count]
            log.info("Dropdown: " + opt.text)
            # time.sleep(2)
            count += 1


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



