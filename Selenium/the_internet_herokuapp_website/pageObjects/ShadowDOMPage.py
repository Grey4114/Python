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

    shadow_Link = (By.XPATH, "//a[text()='Shadow DOM']")        # Main Page link
    shadow_Header = (By.XPATH, "//h1[text()='Simple template']")     # Page header text

    shadow_Text1 = (By.CSS_SELECTOR, "span[slot='my-text']")    # Text 1
    shadow_Text2 = (By.CSS_SELECTOR, "ul[slot='my-text']")      # Text 2


    def shadowDOM_LinkText(self):
        return self.driver.find_element(*ShadowDOMPage.shadow_Link)

    def shadowDOM_HeaderText(self):
        return self.driver.find_element(*ShadowDOMPage.shadow_Header)

    def shadowDOM_Text_1(self):
        return self.driver.find_element(*ShadowDOMPage.shadow_Text1)

    def shadowDOM_Text_2(self):
        return self.driver.find_element(*ShadowDOMPage.shadow_Text2)

