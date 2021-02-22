"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
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
        log.info("TEST PAGE: Checkboxes")
        checkboxes_page.checkboxes_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/checkboxes"
        log.info("URL - Passed: " + url)


        # Verify the Header
        header_text = checkboxes_page.checkbox_HeaderText().text
        assert ("Checkboxes" in header_text)
        log.info("Header - Passed: " + header_text)


        # Verify check/uncheck the boxes
        boxes = checkboxes_page.checkbox_Boxes()
        checks = checkboxes_page.checked_Boxes()
        notchecks = checkboxes_page.notchecked_Boxes()

        for box in boxes:
            box.click()

        assert checks[0]
        assert notchecks[0]
        log.info("Checkboxes - Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()
