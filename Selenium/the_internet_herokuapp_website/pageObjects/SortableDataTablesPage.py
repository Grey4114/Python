"""
Website:  https://the-internet.herokuapp.com/tables
Created:  2/15/2021
Notes:
    Connected Test Object Script - /tests/test_Page_SortableDataTables.py

    This web page seems to be more of an example page then a selenium test page
    Created a test for checking the names in the example 2 list.
"""


from selenium.webdriver.common.by import By


class SortableDataTablesPage:
    def __init__(self, driver):
        self.driver = driver

    sortable_LinkText = (By.XPATH, "//a[text()='Sortable Data Tables']")        # Main Page link
    sortable_Header = (By.XPATH, "//h3[text()='Data Tables']")         # Page header text
    sortable_Table2 = (By.XPATH, "//td[@class='last-name']")


    def sortableDataTables_Link(self):
        return self.driver.find_element(*SortableDataTablesPage.sortable_LinkText)

    def sortableDataTables_HeaderText(self):
        return self.driver.find_element(*SortableDataTablesPage.sortable_Header)

    def sortableDataTables_Table_2_Names(self):
        return self.driver.find_elements(*SortableDataTablesPage.sortable_Table2)

