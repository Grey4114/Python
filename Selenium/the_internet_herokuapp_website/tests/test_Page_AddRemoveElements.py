"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.AddRemoveElementsPage import AddRemoveElementsPage


class TestAddRemoveElements(BaseClass):

    def test_add_remove(self):
        # Enter the Page
        log = self.getLogger()
        add_remove_page = AddRemoveElementsPage(self.driver)
        log.info("TEST START")
        add_remove_page.addRemove_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/add_remove_elements/"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = add_remove_page.addremove_HeaderText().text
        assert ("Add/Remove Elements" in header_text)
        log.info("Header: " + header_text)


        # Verify Add two delete buttons
        add_remove_page.addElement().click()
        add_remove_page.addElement().click()
        assert len(add_remove_page.delElements())
        log.info("Add Buttons: Passed")


        # Verify Removed delete buttons
        delButtons = add_remove_page.delElements()
        for button in delButtons:
            button.click()

        assert not len(add_remove_page.delElements())
        log.info("Removed Buttons: Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()