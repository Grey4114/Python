"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    Data Tables page
    This web page seems to be more of an example page then a selenium test page
    Created a test for checking the names in the example 2 list.
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
        assert url == "https://the-internet.herokuapp.com/tables"
        log.info("URL Passed: " + url)

        # Verify the Header
        header_text = sortableDataTables_page.sortableDataTables_HeaderText().text
        assert ("Data Tables" in header_text)
        log.info("Header Passed: " + header_text)


        # Verify Table 2 Names
        names = ("Smith", "Bach", "Doe", "Conway")
        nameList = sortableDataTables_page.sortableDataTables_Table_2_Names()
        for n in range(len(names)):
            assert names[n] == nameList[n].text

        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()




