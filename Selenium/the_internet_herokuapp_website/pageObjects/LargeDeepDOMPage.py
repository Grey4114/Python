"""
Website:  https://the-internet.herokuapp.com/large
Created:  2/15/2021
Notes:
    Connected Test Object Script - /tests/test_Page_LargeDeepDOM.py
"""

from selenium.webdriver.common.by import By

class LargeDeepDOMPage:
    def __init__(self, driver):
        self.driver = driver

    largeDeep_Link = (By.XPATH, "//a[text()='Large & Deep DOM']")           # Main Page link
    largeDeep_Header = (By.XPATH, "//h3[text()='Large & Deep DOM']")        # Page header text
    largeDeep_Down = (By.XPATH, "//div[@id='sibling-26.2']")                # DOM Down - select 26.2
    largeDeep_Table = (By.XPATH, "//td[normalize-space()='15.25'] ")        # DOM Table - select 15.25


    def largeDeepDOM_LinkText(self):
        return self.driver.find_element(*LargeDeepDOMPage.largeDeep_Link)

    def largeDeepDOM_HeaderText(self):
        return self.driver.find_element(*LargeDeepDOMPage.largeDeep_Header)

    def largeDeepDOM_DownLocation(self):
        return self.driver.find_element(*LargeDeepDOMPage.largeDeep_Down)

    def largeDeepDOM_TableLocation(self):
        return self.driver.find_element(*LargeDeepDOMPage.largeDeep_Table)






