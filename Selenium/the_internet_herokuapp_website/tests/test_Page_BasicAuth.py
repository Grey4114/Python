"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
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

# NOTE - user and pass: admin

class TestBasicAuth(BaseClass):
    def test_basic_auth(self):
        # Enter the Page
        log = self.getLogger()
        basic_auth_page = BasicAuthPage(self.driver)
        log.info("TEST START")
        basic_auth_page.basicAuth_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/basic_auth"
        log.info("URL: " + url)


        # Cannot test at this time
        # Verify incorrect info in pop up
        # time.sleep(10)
        # self.driver.switch_to.alert.dismiss()
        # assert basic_auth_page.basicAuth_NotAuthorizedText().text == "Not authorized"
        # time.sleep(2)
        # self.driver.back()
        # self.driver.refresh()


        # NOTE - Apparently there is only one type of test for this type of pop-up window
        # Verify correct info in pop up
        time.sleep(2)
        self.driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')
        assert basic_auth_page.basicAuth_SuccessText().text == "Congratulations! You must have the proper credentials."


        # Exit back to the previous menu
        log.info("Basic Auth - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


