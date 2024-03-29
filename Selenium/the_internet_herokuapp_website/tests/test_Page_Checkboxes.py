"""
Website:  https://the-internet.herokuapp.com/checkboxes
Created:  2/9/2021
Notes:
    Connected Page Object Script - /pageObjects/CheckboxesPage.py
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.CheckboxesPage import CheckboxesPage


class TestCheckboxes(BaseClass):
    def test_checkboxes(self):
        # Enter the Page
        log = self.getLogger()
        checkboxes_page = CheckboxesPage(self.driver)
        checkboxes_page.checkboxes_LinkText().click()


        # Verify the Header
        header_text = checkboxes_page.checkbox_HeaderText().text
        assert ("Checkboxes" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/checkboxes"
        log.info("URL: " + url)


        # Verify check/uncheck the boxes
        boxes = checkboxes_page.checkbox_Boxes()
        checks = checkboxes_page.checked_Boxes()
        notchecks = checkboxes_page.notchecked_Boxes()

        for box in boxes:
            box.click()

        assert checks[0]
        assert notchecks[0]


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()
