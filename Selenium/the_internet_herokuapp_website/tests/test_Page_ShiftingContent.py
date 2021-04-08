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


        # Verify Example 1 - Menu page Header Text
        shiftingContent_page.shiftingContent_MenuLink().click()
        ex1_header = shiftingContent_page.shiftingContent_Example1_HeaderText().text
        assert ("Shifting Content: Menu Element" in ex1_header)

        # Verify Example 1 - Menu page shifting gallery button
        gallery = shiftingContent_page.shiftingContent_Example1_GalleryButton()
        loc = gallery.location
        # log.info(loc['x'])
        shiftingContent_page.shiftingContent_Example1_ShiftLink().click()
        gallery = shiftingContent_page.shiftingContent_Example1_GalleryButton()
        loc2 = gallery.location
        # log.info(loc2['x'])
        assert loc['x'] - loc2['x'] == 100 # Verify that the button has moved 100 pixels
        self.driver.back()
        self.driver.back()


        # Verify Example 2 - Menu page Header Text
        shiftingContent_page.shiftingContent_ImageLink().click()
        ex2_header = shiftingContent_page.shiftingContent_Example2_HeaderText().text
        assert ("Shifting Content: Image" in ex2_header)

        # Verify Example 2 - Menu page shifting gallery button
        shiftingContent_page.shiftingContent_Example2_ShiftLink().click()
        image = shiftingContent_page.shiftingContent_Example2_ImageShift()
        loc = image.location
        # log.info(loc)

        shiftingContent_page.shiftingContent_Example2_ShiftLink().click()
        image2 = shiftingContent_page.shiftingContent_Example2_ImageShift()
        loc2 = image2.location
        # log.info(loc2)
        assert loc2['x'] - loc['x'] == 100
        self.driver.back()
        self.driver.back()
        # time.sleep(2)



        # Verify Example 3 - Menu page Header Text
        shiftingContent_page.shiftingContent_ListLink().click()
        ex3_header = shiftingContent_page.shiftingContent_Example3_HeaderText().text
        assert ("Shifting Content: List" in ex3_header)

        # Verify Example 3 - Menu page shifting gallery button
        time.sleep(3)
        shiftText = shiftingContent_page.shiftingContent_Example3_TextList().text

        # Writelines() - move all text from the page to a file
        shift_write = open('D:/GitHub/Python/Selenium/the_internet_herokuapp_website/testData/shift_text.txt', 'w')
        shift_write.writelines(shiftText)
        shift_write.close()

        # Readline - Pull all text from the file
        shift_read = open('D:/GitHub/Python/Selenium/the_internet_herokuapp_website/testData/shift_text.txt', 'r')
        read = shift_read.readlines()

        compare = 'Important Information'
        check = False

        for x in read:
            if compare in x:
                # log.info(x)
                check = True
                break

        assert check

        self.driver.back()


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


