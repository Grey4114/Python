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

        # todo - Verify cancel from pop up
        alert = self.driver.switch_to.alert
        time.sleep(5)
        alert.dismiss()
        time.sleep(2)
        # assert (xXxX in xxxx)

        # todo - Verify incorrect info in pop up
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)

        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # todo - Verify incorrect info in pop up
        self.driver.get('http://name:pass@the-internet.herokuapp.com/basic_auth')
        time.sleep(2)
        alert.accept()
        time.sleep(2)

        # assert (xXxX in xxxx)
        # log.info("Elements Passed")



        # todo - Verify correct info in pop up
        self.driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')
        # Exit the Page
        # log.info(header_text + " - All Tests Passed")
        # time.sleep(2)
        self.driver.back()
        self.driver.refresh()


