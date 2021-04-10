"""
Website:  https://the-internet.herokuapp.com/entry_ad
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_EntryAd.py
"""

from selenium.webdriver.common.by import By

class EntryAdPage:
    def __init__(self, driver):
        self.driver = driver

    entry_Link = (By.XPATH, "//a[text()='Entry Ad']")                   # Main Page link
    entry_Header = (By.XPATH, "//h3[text()='Entry Ad']")                # Page header text

    entry_WindowHeader = (By.CSS_SELECTOR, "div[class='modal-title'] h3")     # Modal Window - Header text
    entry_WindowState = (By.XPATH, "//div[@id='modal']")               # Modal Window - State
    entry_WindowClose = (By.XPATH, "//div[@class='modal-footer']")     # Modal Window - Close button


    def entryAd_LinkText(self):
        return self.driver.find_element(*EntryAdPage.entry_Link)

    def entryAd_HeaderText(self):
        return self.driver.find_element(*EntryAdPage.entry_Header)

    def entryAd_ModalWindowHeader(self):
        return self.driver.find_element(*EntryAdPage.entry_WindowHeader)

    def entryAd_ModalWindowState(self):
        return self.driver.find_element(*EntryAdPage.entry_WindowState)

    def entryAd_ModalWindowClose(self):
        return self.driver.find_element(*EntryAdPage.entry_WindowClose)