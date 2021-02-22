"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""

from selenium.webdriver.common.by import By

class ShadowDOMPage:
    def __init__(self, driver):
        self.driver = driver

    shadow_LinkText = (By.XPATH, "//a[text()='Shadow DOM']")
    shadow_Header = (By.XPATH, "//h3[text()='Shadow DOM']")

    # todo - text 1 path
    shadow_Text1 = (By.XPATH, " ")
    # todo - text 2 path
    shadow_Text2 = (By.XPATH, " ")


    def shadowDOM_Link(self):
        return self.driver.find_element(*ShadowDOMPage.shadow_LinkText)

    def shadowDOM_HeaderText(self):
        return self.driver.find_element(*ShadowDOMPage.shadow_Header)

    def shadowDOM_Text_1(self):
        return self.driver.find_element(*ShadowDOMPage.shadow_Text1)

    def shadowDOM_Text_2(self):
        return self.driver.find_element(*ShadowDOMPage.shadow_Text2)

