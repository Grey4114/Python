"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from utilities.BaseClass import BaseClass
from pageObjects.ExitIntentPage import ExitIntentPage

class TestExitIntent(BaseClass):

    def test_exit_intent(self):

        # Enter the Page
        log = self.getLogger()
        exitIntent_page = ExitIntentPage(self.driver)
        log.info("TEST START")
        exitIntent_page.exitIntent_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/exit_intent"
        log.info("URL: " + url)


        # Verify the Header
        header_text = exitIntent_page.exitIntent_HeaderText().text
        assert ("Exit Intent" in header_text)
        log.info("Header: " + header_text)


        # todo - Verify Move mouse - open Modal window
        action = ActionChains(self.driver)
        action.move_by_offset(100, 0).perform()
        time.sleep(5)

        # Verify Modal window header text
        entry = exitIntent_page.exitIntent_ModalWindowHeader().text    # todo - fix
        assert entry in "This is a modal window"
        log.info("Modal Header: " + entry)



        # todo - Verify Modal Window open and close
        modal = exitIntent_page.exitIntent_ModalWindowSate().is_displayed()   # todo - fix
        assert not modal

        time.sleep(2)
        exitIntent_page.exitIntent_ModalWindowClose().click()
        time.sleep(2)
        try:
            modal = exitIntent_page.exitIntent_ModalWindowSate().is_displayed()   # todo - fix
        except NoSuchElementException:
            modal = True

        log.info("Modal Window: Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



