"""
Website:  https://the-internet.herokuapp.com/tinymce
Created:  2/16/2021
Notes:
    Connected Page Object Script - pageObjects/WYSIWYGEditorPage.py
"""

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utilities.BaseClass import BaseClass
from pageObjects.WYSIWYGEditorPage import WYSIWYGEditorPage

class TestWYSIWYG_Editor(BaseClass):
    def test_wysiwyg_editor(self):
        # Enter the Page
        log = self.getLogger()
        wysiwygEditor_page = WYSIWYGEditorPage(self.driver)
        wysiwygEditor_page.WYSIWYGEditor_LinkText().click()


        # Verify the Header
        header_text = wysiwygEditor_page.WYSIWYGEditor_HeaderText().text
        assert ("An iFrame containing" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/tinymce"
        log.info("URL: " + url)


        # Verify enter text into iFrame area
        self.driver.switch_to.frame(wysiwygEditor_page.WYSIWYGEditor_iFrame())
        editor = wysiwygEditor_page.WYSIWYGEditor_Area()
        editor.clear()
        editor.send_keys("Quick Brown Fox Jumps over the lazy dog")
        assert "Quick Brown Fox Jumps over the lazy dog" in wysiwygEditor_page.WYSIWYGEditor_Area().text
        # log.info("iFrame: Passed")
        self.driver.switch_to.default_content()


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

