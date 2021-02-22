"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.DisappearingElementsPage import DisappearingElementsPage

class TestDisappearingElements(BaseClass):

    def test_disappearing_elements(self):

        # Enter the Page
        log = self.getLogger()
        disappearingElements_page = DisappearingElementsPage(self.driver)
        log.info("TEST START")
        disappearingElements_page.disappearingElements_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/disappearing_elements"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = disappearingElements_page.disappearingElements_HeaderText().text
        assert ("Disappearing Elements" in header_text)
        log.info("Header Passed: " + header_text)


        # todo - Verify Home Button & Page
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify About Button & Page
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify Contact Button & Page
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify Portfolio Button & Page
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify Gallery Button & Page - Appear/Disappear
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

