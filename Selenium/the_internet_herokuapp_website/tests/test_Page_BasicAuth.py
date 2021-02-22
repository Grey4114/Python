"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.BasicAuthPage import BasicAuthPage


# todo - add page tests
# todo - grab page header text
# todo - assert header text or other text

class TestBasicAuth(BaseClass):
    # NOTE - user and pass: admin

    def test_basic_auth(self):
        # Enter the Page
        log = self.getLogger()
        basic_auth_page = BasicAuthPage(self.driver)
        log.info("TEST PAGE: Basic Auth")
        basic_auth_page.basicAuth_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/basic_auth"
        log.info("URL - Passed: " + url)


        # Verify the Header
        # header_text = add_remove_page.addremove_HeaderText().text
        # assert ("Add/Remove Elements" in header_text)
        # log.info("Header - Passed: " + header_text)


        # Exit the Page
        # log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



        """
        # user and pass: admin
        # validateText2 = "Confirm OK"
        driver.find_element(By.XPATH, "//a[text()='Basic Auth']").click()
        # time.sleep(2)
        alert = driver.switch_to.alert
        alert.authenticate('admin', 'admin')
        time.sleep(2)
        # alert.send_keys("admin")
        # alert.send_keys(Keys.TAB)
        # time.sleep(2)
        # alert.send_keys("admin")
        # alert.accept()
        # alert.dismiss()
        time.sleep(2)
        # confirmText = confirm.text  # assigns the text to an object
        # assert validateText2 in confirmText
        driver.back()
        driver.refresh()
        time.sleep(2)
        """

