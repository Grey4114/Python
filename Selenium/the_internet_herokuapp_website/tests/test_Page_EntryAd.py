"""
Website:  https://the-internet.herokuapp.com/entry_ad
Created:  2/9/2021
Notes:
    Connected Page Object Script - /pageObjects/EntryAdPage.py

"""

import time
import pytest
from selenium.common.exceptions import NoSuchElementException

from utilities.BaseClass import BaseClass
from pageObjects.EntryAdPage import EntryAdPage

class TestEntryAd(BaseClass):
    def test_entry_ad(self):
        # Enter the Page
        log = self.getLogger()
        entryad_page = EntryAdPage(self.driver)
        entryad_page.entryAd_LinkText().click()


        # Verify the Header
        header_text = entryad_page.entryAd_HeaderText().text
        assert ("Entry Ad" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/entry_ad"
        log.info("URL: " + url)


        # Verify Modal Window open and close
        modal = entryad_page.entryAd_ModalWindowState().is_displayed()
        assert modal    # verify open
        entryad_page.entryAd_ModalWindowClose().click()
        time.sleep(2)


        # Verify Modal Window is closed
        modal = entryad_page.entryAd_ModalWindowState().is_displayed()
        assert not modal


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()
