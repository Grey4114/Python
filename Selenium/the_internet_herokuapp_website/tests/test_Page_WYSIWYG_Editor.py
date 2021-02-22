"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.WYSIWYGEditorPage import WYSIWYGEditorPage

class TestWYSIWYG_Editor(BaseClass):

    def test_wysiwyg_editor(self):
        # Enter the Page
        log = self.getLogger()
        wysiwygEditor_page = WYSIWYGEditorPage(self.driver)
        log.info("TEST START")
        wysiwygEditor_page.WYSIWYGEditor_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/tinymce"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = wysiwygEditor_page.WYSIWYGEditor_HeaderText().text
        assert ("An iFrame containing" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify Area
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify option
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



