"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.TyposPage import TyposPage

class TestTypos(BaseClass):

    def test_typos(self):
        # Enter the Page
        log = self.getLogger()
        typos_page = TyposPage(self.driver)
        log.info("TEST START")
        typos_page.typos_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/typos"
        log.info("URL: " + url)

        # Verify the Header
        header_text = typos_page.typos_HeaderText().text
        assert ("Typos" in header_text)
        log.info("Header: " + header_text)


        # Get all of the text on the page and write it to a file
        page = typos_page.typos_PageText().text
        typos_write = open('D:/GitHub/Python/Selenium/the_internet_herokuapp_website/testData/typos_write.txt', 'w')
        typos_write.writelines(page)
        typos_write.close()

        # Open the text file and get the lines
        typos_write = open('D:/GitHub/Python/Selenium/the_internet_herokuapp_website/testData/typos_write.txt', 'r')
        write = typos_write.readlines()  # Move all of the lines to a variable

        # Using readlines()
        typos_read = open('D:/GitHub/Python/Selenium/the_internet_herokuapp_website/testData/typos_read.txt', 'r')
        read = typos_read.readlines()       # Move all of the lines to a variable

        # Verify that each line is correct - compare to a file with the correct lines
        count = 0
        for x in write:
            assert write[count] == read[count]
            count += 1

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(5)
        self.driver.back()
        self.driver.refresh()




