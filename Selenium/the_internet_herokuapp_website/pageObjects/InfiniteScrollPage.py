"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


class InfiniteScrollPage:
    def __init__(self, driver):
        self.driver = driver

    infinite_LinkText = (By.XPATH, "//a[text()='Infinite Scroll']")
    infinite_Header = (By.XPATH, "//h3[text()='Infinite Scroll']")

    # todo - scroll path
    infinite_Scroll = (By.XPATH, " ")



    def infiniteScroll_Link(self):
        return self.driver.find_element(*InfiniteScrollPage.infinite_LinkText)

    def infiniteScroll_HeaderText(self):
        return self.driver.find_element(*InfiniteScrollPage.infinite_Header)

    def infiniteScroll_Scroll(self):
        return self.driver.find_element(*InfiniteScrollPage.infinite_Scroll)
