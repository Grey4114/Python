"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.JavaScriptOnLoadEventErrorPage import JavaScriptOnloadEventErrorPage

class TestJavaScript_OnloadEventError(BaseClass):

    def test_java_script_onload_event_error(self):
        # Enter the Page
        log = self.getLogger()
        jsOnloadEventErro_page = JavaScriptOnloadEventErrorPage(self.driver)
        log.info("TEST START")
        jsOnloadEventErro_page.js_onloadEventError_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/javascript_error"
        log.info("URL Passed: " + url)

        # todo - Verify the text
        page_text = jsOnloadEventErro_page.js_onloadEventError_PageText().text
        assert ("This page has a JavaScript error in the onload event" in page_text)
        log.info("Text Passed")


        # Exit the Page
        log.info("JavaScript Onload Event - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



