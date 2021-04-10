"""
Website:  https://the-internet.herokuapp.com/javascript_alerts
Created:  2/16/2021
Notes:
    Connected Page Object Script - /pageObjects/JavaScriptAlertsPage.py
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.JavaScriptAlertsPage import JavaScriptAlertsPage

class TestJavaScriptAlerts(BaseClass):
    def test_java_script_alerts(self):
        # Enter the Page
        log = self.getLogger()
        javaScriptAlerts_page = JavaScriptAlertsPage(self.driver)
        javaScriptAlerts_page.javaScriptAlerts_LinkText().click()


        # Verify the Header
        header_text = javaScriptAlerts_page.javaScriptAlerts_HeaderText().text
        assert ("JavaScript Alerts" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/javascript_alerts"
        log.info("URL: " + url)


        # Verify JSAlert window open & close
        javaScriptAlerts_page.javaScriptAlerts_AlertButton().click()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(3)
        assert javaScriptAlerts_page.javaScriptAlerts_Results().text == "You successfully clicked an alert"
        # log.info("JS Alert: " + javaScriptAlerts_page.javaScriptAlerts_Results().text)


        # Verify JSConfirm - Cancel
        javaScriptAlerts_page.javaScriptAlerts_ConfirmButton().click()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        alert.dismiss()
        time.sleep(3)
        assert javaScriptAlerts_page.javaScriptAlerts_Results().text == "You clicked: Cancel"
        # log.info("JS Confirm: " + javaScriptAlerts_page.javaScriptAlerts_Results().text)


        # Verify JSConfirm - Cancel
        javaScriptAlerts_page.javaScriptAlerts_ConfirmButton().click()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(3)
        assert javaScriptAlerts_page.javaScriptAlerts_Results().text == "You clicked: Ok"
        # log.info("JS Confirm: " + javaScriptAlerts_page.javaScriptAlerts_Results().text)


        # Verify JS Prompt - Cancel
        javaScriptAlerts_page.javaScriptAlerts_PromptButton().click()
        # time.sleep(3)
        alert = self.driver.switch_to.alert
        alert.dismiss()
        # time.sleep(3)
        assert javaScriptAlerts_page.javaScriptAlerts_Results().text == "You entered: null"
        # log.info("JS Prompt: " + javaScriptAlerts_page.javaScriptAlerts_Results().text)


        # Verify JS Prompt - OK w/Empty Text Field
        javaScriptAlerts_page.javaScriptAlerts_PromptButton().click()
        # time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        # time.sleep(2)
        assert javaScriptAlerts_page.javaScriptAlerts_Results().text == "You entered:"
        # log.info("JS Prompt: " + javaScriptAlerts_page.javaScriptAlerts_Results().text)


        # Verify JS Prompt - OK w/Text Field
        javaScriptAlerts_page.javaScriptAlerts_PromptButton().click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.send_keys("test")
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        assert javaScriptAlerts_page.javaScriptAlerts_Results().text == "You entered: test"
        # log.info("JS Prompt: " + javaScriptAlerts_page.javaScriptAlerts_Results().text)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


