"""
Website:  https://the-internet.herokuapp.com/exit_intent
Created:  2/9/2021
Notes:
    Connected Page Object Script - /pageObjects/ExitIntentPage.py

    - Unable to find a way to select outside of the page
    - Could not find a website that showed a way to do this
"""

import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from utilities.BaseClass import BaseClass
from pageObjects.ExitIntentPage import ExitIntentPage

# TODO - Need to do more research into how to click outside the page

class TestExitIntent(BaseClass):
    def test_exit_intent(self):
        # Enter the Page
        log = self.getLogger()
        exitIntent_page = ExitIntentPage(self.driver)
        log.info("TEST START")
        exitIntent_page.exitIntent_LinkText().click()


        # Verify the Header
        header_text = exitIntent_page.exitIntent_HeaderText().text
        assert ("Exit Intent" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/exit_intent"
        log.info("URL: " + url)


        # Verify Move mouse - open Modal window
        # action = ActionChains(self.driver)
        # exitPage = exitIntent_page.exitIntent_WindowOutside()
        # action.move_by_offset(0, 0).click().perform()
        # time.sleep(5)


        # Verify Modal Window open and close
        # modal = exitIntent_page.exitIntent_ModalWindowSate().is_displayed()
        # assert not modal
        # time.sleep(2)
        # exitIntent_page.exitIntent_ModalWindowClose().click()
        # time.sleep(2)
        #try:
        #     modal = exitIntent_page.exitIntent_ModalWindowSate().is_displayed()
        # except NoSuchElementException:
        #     modal = True
        # log.info("Modal Window: Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



