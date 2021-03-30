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
from pageObjects.ContextMenuPage import ContextMenuPage

class TestContextMenu(BaseClass):

    def test_contex_menu(self):
        # Enter the Page
        log = self.getLogger()
        contextmenu_page = ContextMenuPage(self.driver)
        log.info("TEST START")
        contextmenu_page.contextMenu_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/context_menu"
        log.info("URL: " + url)


        # Verify the Header
        header_text = contextmenu_page.contextMenu_HeaderText().text
        assert ("Context Menu" in header_text)
        log.info("Header: " + header_text)

        # Grab page handle
        window_before = self.driver.window_handles[0]      # Page window


        # Right click Context box & Verify Alert message
        action = ActionChains(self.driver)
        action.context_click(contextmenu_page.contextMenu_RightClickBox()).perform()
        # time.sleep(5)

        # Verify Alert message & Dismiss alert box
        alert = self.driver.switch_to.alert
        alertText = alert.text
        assert ('You selected a context menu' in alertText)
        log.info("Alert Text: " + alertText)
        time.sleep(5)
        alert.accept()
        time.sleep(5)


        # todo - Verify & Dismiss popup box
        window_after = self.driver.window_handles[0]       # Popup window
        self.driver.switch_to.window().send_keys(Keys.ESCAPE)
        time.sleep(5)



        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        # time.sleep(2)
        self.driver.back()
        self.driver.refresh()

