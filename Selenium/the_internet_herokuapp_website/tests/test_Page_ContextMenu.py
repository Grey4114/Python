"""
Website:  https://the-internet.herokuapp.com/context_menu
Created:  2/9/2021
Notes:
    Connected Page Object Script - /pageObjects/ContextMenuPage.py

    ** Unable to interact with windows pop up box using selenium python at this time
    ** Accoring to internet sites this cannot be done in selenium
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
        contextmenu_page.contextMenu_LinkText().click()

        # Verify the Header
        header_text = contextmenu_page.contextMenu_HeaderText().text
        assert ("Context Menu" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/context_menu"
        log.info("URL: " + url)


        # Grab page handle
        window_before = self.driver.window_handles[0]      # Page window

        # Right click Context box & Verify Alert message
        action = ActionChains(self.driver)
        action.context_click(contextmenu_page.contextMenu_RightClickBox()).perform()
        action.send_keys(Keys.ESCAPE)

        # Verify Alert message & Dismiss alert box
        alert = self.driver.switch_to.alert
        alertText = alert.text
        assert ('You selected a context menu' in alertText)
        alert.accept()
        time.sleep(5)


        # ** UNABLE TO GET TO WORK AT THIS TIME - Verify & Dismiss windows popup box
        # action.context_click().send_keys(Keys.BACKSPACE).perform()
        # self.driver.switch_to.window(self.driver.window_handles[0])   # Popup window
        # window.close()
        # self.driver.quit()
        # self.driver
        # time.sleep(5)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

