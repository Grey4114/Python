"""
Website:  https://the-internet.herokuapp.com/jqueryui/menu
Created:  2/16/2021
Notes:
    Connected Page Object Script - /pageObjects/JQueryUIMenusPage.py

"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.JQueryUIMenusPage import JQueryUIMenusPage

# TODO - Not sure how to properly verify these tests at this time

class TestJQueryUIMenus(BaseClass):
    def test_jquery_ui_menus(self):
        # Enter the Page
        log = self.getLogger()
        jqueryUIMenus_page = JQueryUIMenusPage(self.driver)
        log.info("TEST START")
        jqueryUIMenus_page.jQueryUIMenus_LinkText().click()


        # Verify the Header
        header_text = jqueryUIMenus_page.jQueryUIMenus_HeaderText().text
        assert ("JQueryUI" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/jqueryui/menu"
        log.info("URL: " + url)


        # Verify Enabled
        time.sleep(2)
        enable = jqueryUIMenus_page.jQueryUIMenus_EnabledLink()
        self.driver.execute_script("arguments[0].click()", enable)
        time.sleep(2)
        # assert (xXxX in xxxx)


        # Verify Enabled downloads pdf
        pdf = jqueryUIMenus_page.jQueryUIMenus_Downloads_PDF()
        self.driver.execute_script("arguments[0].click()", pdf)
        time.sleep(2)
        # assert (xXxX in xxxx)


        # Verify Enabled downloads csv
        csv = jqueryUIMenus_page.jQueryUIMenus_Downloads_CSV()
        self.driver.execute_script("arguments[0].click()", csv)
        time.sleep(2)
        # assert (xXxX in xxxx)


        # Verify Enabled downloads xml
        xml = jqueryUIMenus_page.jQueryUIMenus_Downloads_XML()
        self.driver.execute_script("arguments[0].click()", xml)
        time.sleep(2)
        # assert (xXxX in xxxx)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



