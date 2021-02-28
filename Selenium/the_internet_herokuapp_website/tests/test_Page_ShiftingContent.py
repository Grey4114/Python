"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.ShiftingContentPage import ShiftingContentPage


class TestShiftingContent(BaseClass):

    def test_shifting_content(self):
        # Enter the Page
        log = self.getLogger()
        shiftingContent_page = ShiftingContentPage(self.driver)
        log.info("TEST START")
        shiftingContent_page.shiftingContent_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/shifting_content"
        log.info("URL: " + url)

        # Verify the Header
        header_text = shiftingContent_page.shiftingContent_HeaderText().text
        assert ("Shifting Content" in header_text)
        log.info("Header: " + header_text)


        # todo - Verify Menu page
        shiftingContent_page.shiftingContent_MenuLink().click()
        ex1_header = shiftingContent_page.shiftingContent_Example1_HeaderText().text
        assert ("Shifting Content: Menu Element" in ex1_header)
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify Image page
        shiftingContent_page.shiftingContent_ImageLink().click()
        ex2_header = shiftingContent_page.shiftingContent_Example2_HeaderText().text
        assert ("Shifting Content: Image" in ex2_header)
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify List page
        shiftingContent_page.shiftingContent_ListLink().click()
        ex3_header = shiftingContent_page.shiftingContent_Example3_HeaderText().text
        assert ("Shifting Content: List" in ex3_header)
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")




        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




"Et numquam et aliquam."

"Nesciunt autem eum odit fuga tempora deleniti."

"Vel aliquid dolores veniam enim nesciunt libero quaerat."

"Important Information You're Looking For"

"Sed deleniti blanditiis odio laudantium."


