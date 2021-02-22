"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Dynamic Loading page
"""

from selenium.webdriver.common.by import By

class EntryAdPage:
    def __init__(self, driver):
        self.driver = driver

    entry_LinkText = (By.XPATH, "//a[text()='Entry Ad']")
    entry_Header = (By.XPATH, "//h3[text()='Entry Ad']")

    # todo - window header text path
    entry_WindowHeader = (By.XPATH, "")
    # todo - window close path
    entry_WindowClose = (By.XPATH, "")
    # todo - click here path
    entry_ClickHere = (By.XPATH, "")


    def entryAd_Link(self):
        return self.driver.find_element(*EntryAdPage.entry_LinkText)

    def entryAd_HeaderText(self):
        return self.driver.find_element(*EntryAdPage.entry_Header)

    def entryAd_WindowHeader(self):
        return self.driver.find_element(*EntryAdPage.entry_WindowHeader)

    def entryAd_WindowClose(self):
        return self.driver.find_element(*EntryAdPage.entry_WindowClose)

    def entryAd_ClickHere(self):
        return self.driver.find_element(*EntryAdPage.entry_ClickHere)
