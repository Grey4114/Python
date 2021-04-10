"""
Website:  https://the-internet.herokuapp.com/inputs
Created:  2/16/2021
Notes:
    Connected Page Object Script - /pageObjects/InputsPage.py
"""

import time
import pytest
from selenium.webdriver.common.keys import Keys

from utilities.BaseClass import BaseClass
from pageObjects.InputsPage import InputsPage

class TestInputs(BaseClass):
    def test_inputs(self):
        # Enter the Page
        log = self.getLogger()
        inputs_page = InputsPage(self.driver)
        inputs_page.inputs_LinkText().click()


        # Verify the Header
        header_text = inputs_page.inputs_HeaderText().text
        assert ("Inputs" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/inputs"
        log.info("URL: " + url)


        # Verify decrease number value
        time.sleep(2)
        for x in range(0, 5):
            inputs_page.inputs_NumberField().send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        assert inputs_page.inputs_NumberField().get_attribute('value') == '-5'
        # log.info("Decrease: " + inputs_page.inputs_NumberField().get_attribute('value'))


        # Verify increase number value
        for x in range(0, 10):
            inputs_page.inputs_NumberField().send_keys(Keys.ARROW_UP)
        time.sleep(2)
        assert inputs_page.inputs_NumberField().get_attribute('value') == '5'
        # log.info("Increase: " + inputs_page.inputs_NumberField().get_attribute('value'))


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



