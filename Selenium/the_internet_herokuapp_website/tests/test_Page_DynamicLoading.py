"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass
from pageObjects.DynamicLoadingPage import DynamicLoadingPage


class TestDynamicLoading(BaseClass):

    def test_dynamic_loading(self):
        # Enter the Page
        log = self.getLogger()
        dynamicLoading_page = DynamicLoadingPage(self.driver)
        log.info("TEST START")
        dynamicLoading_page.dynamicLoading_LinkText().click()
        wait = WebDriverWait(self.driver, 10)  # Waits 10 seconds when called


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/dynamic_loading"
        log.info("URL: " + url)


        # Verify the Header
        header_text = dynamicLoading_page.dynamicLoading_HeaderText().text
        assert ("Dynamically Loaded Page Elements" in header_text)
        log.info("Header: " + header_text)


        # Example 1 - Verify text is hidden on the page
        dynamicLoading_page.dynamicLoading_ExampleLink_1().click()
        display = dynamicLoading_page.dynamicLoading_ExampleHello_1().is_displayed()
        assert not display

        dynamicLoading_page.dynamicLoading_ExampleStart_1().click()
        wait.until(EC.visibility_of_element_located((By.ID, "finish")))  # Explicit Wait - Targeted Wait
        display = dynamicLoading_page.dynamicLoading_ExampleHello_1().is_displayed()
        assert display
        log.info("Example 1: Passed")
        self.driver.back()



        # Example 2 - Verify text is not on the page
        dynamicLoading_page.dynamicLoading_ExampleLink_2().click()
        try:
            display = dynamicLoading_page.dynamicLoading_ExampleHello_2().text
        except NoSuchElementException:
            display = "No Message"
        assert display == "No Message"

        dynamicLoading_page.dynamicLoading_ExampleStart_2().click()
        wait.until(EC.presence_of_element_located((By.ID, "finish")))  # Explicit Wait - Targeted Wait
        display = dynamicLoading_page.dynamicLoading_ExampleHello_2().is_displayed()
        assert display
        log.info("Example 2: Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



