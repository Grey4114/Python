"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    Connected Web Page Info - pageObjects/StatusCodesPage.py
"""

import time
import pytest
import requests
from utilities.BaseClass import BaseClass
from pageObjects.StatusCodesPage import StatusCodesPage

class TestStatusCodes(BaseClass):
    def test_status_codes(self):
        # Enter the Page
        log = self.getLogger()
        statusCodes_page = StatusCodesPage(self.driver)
        log.info("TEST START")
        statusCodes_page.statusCodes_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/status_codes"
        log.info("URL: " + url)

        # Verify the Header
        header_text = statusCodes_page.statusCodes_HeaderText().text
        assert ("Status Codes" in header_text)
        log.info("Header: " + header_text)


        # Verify Error code 200
        statusCodes_page.statusCodes_Code200().click()
        req = requests.get("https://the-internet.herokuapp.com/status_codes/200")
        assert req.status_code == 200
        # log.info(req.status_code)
        # time.sleep(3)
        self.driver.back()
        self.driver.refresh()


        # Verify Error code 301
        statusCodes_page.statusCodes_Code301().click()
        req = requests.get("https://the-internet.herokuapp.com/status_codes/301")
        assert req.status_code == 301
        # log.info(req.status_code)
        # time.sleep(3)
        self.driver.back()
        self.driver.refresh()


        # Verify Error code 404
        statusCodes_page.statusCodes_Code404().click()
        req = requests.get("https://the-internet.herokuapp.com/status_codes/404")
        assert req.status_code == 404
        # log.info(req.status_code)
        # time.sleep(3)
        self.driver.back()
        self.driver.refresh()


        # Verify Error code 500
        statusCodes_page.statusCodes_Code500().click()
        req = requests.get("https://the-internet.herokuapp.com/status_codes/500")
        assert req.status_code == 500
        # log.info(req.status_code)
        # time.sleep(3)
        self.driver.back()


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



