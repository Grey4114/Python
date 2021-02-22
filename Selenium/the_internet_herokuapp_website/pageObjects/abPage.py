"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the AB Testing page objects
"""

from selenium.webdriver.common.by import By


class abPage:
    def __init__(self, driver):
        self.driver = driver

    ab_LinkText = (By.XPATH, "//a[text()='A/B Testing']")               # Main Website link to page
    ab_Header_1 = (By.XPATH, "//h3[text()='A/B Test Control']")         # Page header text
    ab_Header_2 = (By.XPATH, "//h3[text()='A/B Test Variation 1']")     # Page header text


    def ab_Link(self):
        return self.driver.find_element(*abPage.ab_LinkText)

    def ab_HeaderText_1(self):
        return self.driver.find_element(*abPage.ab_Header_1)

    def ab_HeaderText_2(self):
        return self.driver.find_element(*abPage.ab_Header_2)

