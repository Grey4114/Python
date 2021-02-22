"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


class SortableDataTablesPage:
    def __init__(self, driver):
        self.driver = driver

    sortable_LinkText = (By.XPATH, "//a[text()='Sortable Data Tables']")
    sortable_Header = (By.XPATH, "//h3[text()='Sortable Data Tables']")

    # todo - Table 1
    sortable_Table1 = (By.XPATH, " ")
    # todo - Table 2
    sortable_Table2 = (By.XPATH, " ")



    def sortableDataTables_Link(self):
        return self.driver.find_element(*SortableDataTablesPage.sortable_LinkText)

    def sortableDataTables_HeaderText(self):
        return self.driver.find_element(*SortableDataTablesPage.sortable_Header)

    def sortableDataTables_Table_1(self):
        return self.driver.find_element(*SortableDataTablesPage.sortable_Table1)

    def sortableDataTables_Table_2(self):
        return self.driver.find_element(*SortableDataTablesPage.sortable_Table2)

