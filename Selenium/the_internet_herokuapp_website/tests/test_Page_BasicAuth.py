"""
Website:  https://the-internet.herokuapp.com/basic_auth
Created:  2/9/2021
Notes:
    Connected Page Object Script - /pageObjects/BasicAuthPage.py

    - user and pass: admin
    - No page header text
    - Apparently there is only one way to test this type of pop-up Auth window
    - According to the internet there is no way to test cancel button or false user/pass for the pop-up Auth window

    ** Digest Authentication & Secure File Download pages have the same issues as this page
"""

import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

from utilities.BaseClass import BaseClass
from pageObjects.BasicAuthPage import BasicAuthPage

class TestBasicAuth(BaseClass):
    def test_basic_auth(self):
        # Enter the Page
        log = self.getLogger()
        basic_auth_page = BasicAuthPage(self.driver)
        basic_auth_page.basicAuth_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/basic_auth"
        log.info("URL: " + url)


        # Verify correct info in pop up
        time.sleep(2)
        self.driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')
        assert basic_auth_page.basicAuth_SuccessText().text == "Congratulations! You must have the proper credentials."


        # Exit back to the previous menu
        log.info("Basic Auth - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


