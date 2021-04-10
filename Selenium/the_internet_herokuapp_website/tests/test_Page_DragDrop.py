"""
Website:  https://the-internet.herokuapp.com/drag_and_drop
Created:  2/9/2021
Notes:
    Connected Page Object Script - /pageObjects/DragDropPage.py

    - Unable to get this to work at this time, various websites claim it ia a broken feature
"""

import time
import pytest
from selenium.webdriver import ActionChains
# from seletools.actions import drag_and_drop    - Not working

from utilities.BaseClass import BaseClass
from pageObjects.DragDropPage import DragDropPage

# Todo - Broken drag and drop feature - try to fix in the future

class TestDragDrop(BaseClass):
    def test_drag_and_drop(self):
        # Enter the Page
        log = self.getLogger()
        dragdrop_page = DragDropPage(self.driver)
        dragdrop_page.dragDrop_LinkText().click()


        # Verify the Header
        header_text = dragdrop_page.dragDrop_HeaderText().text
        assert ("Drag and Drop" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/drag_and_drop"
        log.info("URL: " + url)



        # Verify drag A to B
        # Action Chains - not working
        # action = ActionChains(self.driver)
        # boxA = dragdrop_page.dragDrop_Box_A()
        # boxB = dragdrop_page.dragDrop_Box_B()
        # action.click_and_hold(boxA).move_to_element(boxB).click(boxB).perform()

        # Seletools - Not working
        # boxA = dragdrop_page.dragDrop_Box_A()
        # boxB = dragdrop_page.dragDrop_Box_B()
        # drag_and_drop(self.driver, boxA, boxB)

        # time.sleep(5)
        # boxA = dragdrop_page.dragDrop_Box_A()
        # boxB = dragdrop_page.dragDrop_Box_B()
        # assert (boxA_text == "B" and boxB_text == "A")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



