"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from selenium.common.exceptions import NoSuchElementException

from utilities.BaseClass import BaseClass
from pageObjects.DynamicControlsPage import DynamicControlsPage

class TestDynamicControls(BaseClass):

    def test_dynamic_controls(self):

        # Enter the Page
        log = self.getLogger()
        dynamicControls_page = DynamicControlsPage(self.driver)
        log.info("TEST START")
        dynamicControls_page.dynamicControls_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/dynamic_controls"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = dynamicControls_page.dynamicControls_HeaderText().text
        assert ("Dynamic Controls" in header_text)
        log.info("Header Passed: " + header_text)


        # Verify Remove button - checkbox removal & message text
        messagetext = "No Message"      # Place holder
        dynamicControls_page.dynamicControls_AddRemoveButton().click()
        time.sleep(10)      # todo - replace with Wait
        try:
            dynamicControls_page.dynamicControls_Checkbox().click()
        except NoSuchElementException:
            messagetext = dynamicControls_page.dynamicControls_MessageText().text

        assert messagetext == "It's gone!"
        log.info("Add/Remove Button: " + messagetext)


        # Verify Enable button - enable text box & message text
        dynamicControls_page.dynamicControls_EnableDisableButton().click()
        time.sleep(10)      # todo - replace with Wait
        try:
            dynamicControls_page.dynamicControls_TextField().click()
            messagetext = dynamicControls_page.dynamicControls_MessageText().text
        except NoSuchElementException:
            messagetext = "No Message"

        assert messagetext == "It's enabled!"
        log.info("Enable/Disable Button: " + messagetext)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



