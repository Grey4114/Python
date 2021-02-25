"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from selenium.webdriver import ActionChains

from utilities.BaseClass import BaseClass
from pageObjects.DragDropPage import DragDropPage


class TestDragDrop(BaseClass):

    def test_drag_and_drop(self):

        # Enter the Page
        log = self.getLogger()
        dragdrop_page = DragDropPage(self.driver)
        log.info("TEST START")
        dragdrop_page.dragDrop_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/drag_and_drop"
        log.info("URL: " + url)


        # Verify the Header
        header_text = dragdrop_page.dragDrop_HeaderText().text
        assert ("Drag and Drop" in header_text)
        log.info("Header: " + header_text)



        # todo - Verify drag A to B
        boxA = dragdrop_page.dragDrop_Box_A()
        boxB = dragdrop_page.dragDrop_Box_B()
        boxA_text = dragdrop_page.dragDrop_Box_A().text
        boxB_text = dragdrop_page.dragDrop_Box_B().text

        log.info("a = " + boxA_text + " & " + "b = " + boxB_text)   # quick check

        action = ActionChains(self.driver)
        action.click_and_hold(boxA).pause(3).move_to_element(boxB).release(boxB).perform()
        #action.drag_and_drop(boxA, boxB).perform()

        assert (boxA_text == "B" and boxB_text == "A")
        log.info("Drag & Drop: Passed")




        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



