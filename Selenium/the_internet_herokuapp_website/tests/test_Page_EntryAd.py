"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
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
        log.info("TEST START")
        entryad_page.entryAd_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/entry_ad"
        log.info("URL: " + url)


        # Verify the Header
        header_text = entryad_page.entryAd_HeaderText().text
        assert ("Entry Ad" in header_text)
        log.info("Header: " + header_text)


        # Verify Modal window header text
        entry = entryad_page.entryAd_ModalWindowHeader().text    # todo - fix
        assert entry in "This is a modal window"
        log.info("Modal Header: " + entry)

        # todo - Verify Modal Window open and close
        modal = entryad_page.entryAd_ModalWindowState().is_displayed()   # todo - fix
        assert not modal

        time.sleep(2)
        entryad_page.entryAd_ModalWindowClose().click()
        time.sleep(2)
        try:
            modal = entryad_page.entryAd_ModalWindowState().is_displayed()   # todo - fix
        except NoSuchElementException:
            modal = True

        log.info("Modal Window: Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

