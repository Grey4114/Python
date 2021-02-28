"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.SortableDataTablesPage import SortableDataTablesPage

class TestSortableDataTables(BaseClass):

    def test_Sortable_data_tables(self):
        # Enter the Page
        log = self.getLogger()
        sortableDataTables_page = SortableDataTablesPage(self.driver)
        log.info("TEST START")
        sortableDataTables_page.sortableDataTables_Link().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://xxxx/xxxx"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = sortableDataTables_page.sortableDataTables_HeaderText().text
        assert ("Data Tables" in header_text)
        log.info("Header Passed: " + header_text)


        # todo - not sure how to test this
        # todo - Verify table 1
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # todo - Verify table 2
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




