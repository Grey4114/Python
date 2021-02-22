"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.DragDropPage import DragDropPage


class TestDragDrop(BaseClass):

    def test_drag_and_drop(self):

        # Enter the Page
        log = self.getLogger()
        dragdrop_page = DragDropPage(self.driver)
        log.info("TEST START")
        dragdrop_page.dragDrop_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/drag_and_drop"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = dragdrop_page.dragDrop_HeaderText().text
        assert ("Drag and Drop" in header_text)
        log.info("Header Passed: " + header_text)

        # todo - Verify drag A to B
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify drag B to A
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



