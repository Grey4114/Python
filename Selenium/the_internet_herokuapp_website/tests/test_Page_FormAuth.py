"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    username: tomsmith
    password: SuperSecretPassword!
"""

import time
import pytest
from selenium.webdriver.common.keys import Keys

from utilities.BaseClass import BaseClass
from pageObjects.FormAuthPage import FormAuthPage


class TestFormAuth(BaseClass):

    def test_form_authorities(self):
        # Enter the Page
        log = self.getLogger()
        formAuth_page = FormAuthPage(self.driver)
        log.info("TEST START")
        formAuth_page.formAuth_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/login"
        log.info("URL: " + url)

        # Verify the Header
        header_text = formAuth_page.formAuth_HeaderText().text
        assert ("Login Page" in header_text)
        log.info("Header: " + header_text)


        # Verify Invalid login
        formAuth_page.formAuth_Username().send_keys("Test")
        formAuth_page.formAuth_Password().send_keys("Test")
        formAuth_page.formAuth_LoginButton().click()
        invalid = formAuth_page.formAuth_InvalidText().text
        assert "Your username is invalid!" in invalid
        # time.sleep(3)


        # Verify Valid login
        formAuth_page.formAuth_Username().send_keys("tomsmith")
        formAuth_page.formAuth_Password().send_keys("SuperSecretPassword!")
        formAuth_page.formAuth_LoginButton().click()
        valid = formAuth_page.formAuth_ValidText().text
        assert "You logged into a secure area!" in valid
        # time.sleep(3)


        # Verify Logout
        formAuth_page.formAuth_LogoutButton().click()
        loggedout = formAuth_page.formAuth_ValidText().text
        assert "You logged out of the secure area!" in loggedout
        log.info("Login Check: Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

