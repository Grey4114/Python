"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.ForgotPasswordPage import ForgotPasswordPage

class TestForgotPassword(BaseClass):

    def test_forgot_password(self):
        # Enter the Page
        log = self.getLogger()
        forgotPassword_page = ForgotPasswordPage(self.driver)
        log.info("TEST START")
        forgotPassword_page.forgotPassword_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/forgot_password"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = forgotPassword_page.forgotPassword_HeaderText().text
        assert ("Forgot Password" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify retrieve password
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




