"""
Website:  https://the-internet.herokuapp.com/slow
Created:  2/15/2021
Notes:
    Connected Test Object Script - /tests/test_Page_SlowResources.py
"""


from selenium.webdriver.common.by import By

class SlowResourcesPage:
    def __init__(self, driver):
        self.driver = driver

    slow_Link = (By.XPATH, "//a[text()='Slow Resources']")      # Main Page link
    slow_Header = (By.XPATH, "//h3[text()='Slow Resources']")       # Page header text


    def slowResources_LinkText(self):
        return self.driver.find_element(*SlowResourcesPage.slow_Link)

    def slowResources_HeaderText(self):
        return self.driver.find_element(*SlowResourcesPage.slow_Header)



