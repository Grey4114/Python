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

from utilities.BaseClass import BaseClass
from pageObjects.DigestAuthPage import DigestAuthPage

# user and pass: admin

class TestDigestAuth(BaseClass):

    def test_digest_auth(self):
        # Enter the Page
        log = self.getLogger()
        digestauth_page = DigestAuthPage(self.driver)
        log.info("TEST START")
        digestauth_page.digestAuth_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/digest_auth"
        log.info("URL: " + url)


        # Verify enter a valid user & pass
        self.driver.get('http://admin:admin@the-internet.herokuapp.com/digest_auth')
        time.sleep(2)
        assert digestauth_page.digestAuth_SuccessLogin().text == "Congratulations! You must have the proper credentials."

        # Todo - Verify invalid name/pass and click on cancel
        # unable to get a fail situation to work at this time
        self.driver.back()
        self.driver.back()
        self.driver.refresh()
        time.sleep(5)
        action = ActionChains(self.driver)
        self.driver.get('http://fail:fail@the-internet.herokuapp.com/digest_auth')
        time.sleep(2)
        action.send_keys(Keys.CANCEL)
        time.sleep(2)
        # assert digestauth_page.digestAuth_SuccessLogin().text == "Not Found"



        # Exit the Page
        log.info("Digital Auth - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



