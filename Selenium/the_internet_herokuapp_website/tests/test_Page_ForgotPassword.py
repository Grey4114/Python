"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from selenium.webdriver.common.keys import Keys

from utilities.BaseClass import BaseClass
from pageObjects.ForgotPasswordPage import ForgotPasswordPage

class TestForgotPassword(BaseClass):

    def test_forgot_password(self):
        # Enter the Page
        log = self.getLogger()
        forgotPassword_page = ForgotPasswordPage(self.driver)
        log.info("TEST START")
        forgotPassword_page.forgotPassword_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/forgot_password"
        log.info("URL: " + url)


        # Verify the Header
        header_text = forgotPassword_page.forgotPassword_HeaderText().text
        assert ("Forgot Password" in header_text)
        log.info("Header: " + header_text)


        # Verify retrieve password
        # time.sleep(3)
        emailfield = forgotPassword_page.forgotPassword_EmailField()
        emailfield.send_keys("TEST")
        # time.sleep(3)
        forgotPassword_page.forgotPassword_RetrieveButton().click()
        fail = forgotPassword_page.forgotPassword_InterServerError().text
        assert fail == "Internal Server Error"
        log.info("Check: Passed")
        # time.sleep(3)

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




