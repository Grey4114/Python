"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.JQueryUIMenusPage import JQueryUIMenusPage

class TestJQueryUIMenus(BaseClass):

    def test_jquery_ui_menus(self):

        # Enter the Page
        log = self.getLogger()
        jqueryUIMenus_page = JQueryUIMenusPage(self.driver)
        log.info("TEST START")
        jqueryUIMenus_page.jQueryUIMenus_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/jqueryui/menu"
        log.info("URL: " + url)

        # Verify the Header
        header_text = jqueryUIMenus_page.jQueryUIMenus_HeaderText().text
        assert ("JQueryUI-Menu" in header_text)
        log.info("Header: " + header_text)


        # todo - Verify Disabled
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # todo - Verify Enabled downloads pdf
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # todo - Verify Enabled downloads csv
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # todo - Verify Enabled downloads xml
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # todo - Verify Enabled back header text
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # todo - Verify Enabled menu
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



