"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.JavaScriptAlertsPage import JavaScriptAlertsPage

class TestJavaScriptAlerts(BaseClass):

    def test_java_script_alerts(self):

        # Enter the Page
        log = self.getLogger()
        javaScriptAlerts_page = JavaScriptAlertsPage(self.driver)
        log.info("TEST START")
        javaScriptAlerts_page.javaScriptAlerts_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/javascript_alerts"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = javaScriptAlerts_page.javaScriptAlerts_HeaderText().text
        assert ("JavaScript Alerts" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify JS Alert page
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify JS Confirm
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify JS Prompt
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


