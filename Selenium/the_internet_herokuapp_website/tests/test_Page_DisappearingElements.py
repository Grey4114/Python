"""
Website:  https://the-internet.herokuapp.com/disappearing_elements
Created:  2/9/2021
Notes:
    Connected Page Object Script - /pageObjects/DisappearingElementsPage.py
"""

import time
import pytest
from selenium.common.exceptions import NoSuchElementException

from utilities.BaseClass import BaseClass
from pageObjects.DisappearingElementsPage import DisappearingElementsPage


class TestDisappearingElements(BaseClass):
    main_url = "https://the-internet.herokuapp.com/"
    disappear_url = "https://the-internet.herokuapp.com/disappearing_elements"
    about_url = "https://the-internet.herokuapp.com/about/"
    contact_url = "https://the-internet.herokuapp.com/contact-us/"
    portfolio_url = "https://the-internet.herokuapp.com/portfolio/"
    gallery_url = "https://the-internet.herokuapp.com/gallery/"


    def test_disappearing_elements(self):
        # Enter the Page
        log = self.getLogger()
        disappearingElements_page = DisappearingElementsPage(self.driver)
        disappearingElements_page.disappearingElements_LinkText().click()


        # Verify the Header
        header_text = disappearingElements_page.disappearingElements_HeaderText().text
        assert ("Disappearing Elements" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == TestDisappearingElements.disappear_url
        log.info("URL: " + url)


        # Verify Home Button to Main (test not required - just for practice)
        disappearingElements_page.disappearingElements_HomeButton().click()
        url = self.driver.current_url
        assert url == TestDisappearingElements.main_url
        self.driver.back()


        # Verify About Button to blank page (test not required - just for practice)
        disappearingElements_page.disappearingElements_AboutButton().click()
        url = self.driver.current_url
        assert url == TestDisappearingElements.about_url
        self.driver.back()


        # Verify Contact Button to blank page (test not required - just for practice)
        disappearingElements_page.disappearingElements_ContactButton().click()
        url = self.driver.current_url
        assert url == TestDisappearingElements.contact_url
        self.driver.back()


        # Verify Portfolio Button to blank page (test not required - just for practice)
        disappearingElements_page.disappearingElements_PortfilioButton().click()
        url = self.driver.current_url
        assert url == TestDisappearingElements.portfolio_url
        self.driver.back()


        # Verify Gallery Button - Appear/Disappear
        check = True
        while check:
            try:
                gallery = disappearingElements_page.disappearingElements_GalleryButton().text
                self.driver.refresh()
            except NoSuchElementException:
                check = False


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

