"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.FormAuthPage import FormAuthPage

class TestFormAuth(BaseClass):

    def test_form_authorities(self):
        # Enter the Page
        log = self.getLogger()
        formAuth_page = FormAuthPage(self.driver)
        log.info("TEST START")
        formAuth_page.formAuth_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/login"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = formAuth_page.formAuth_HeaderText().text
        assert ("Login Page" in header_text)
        log.info("Header Passed: " + header_text)



        # todo - Verify valid login
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify invalid login
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")



        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




