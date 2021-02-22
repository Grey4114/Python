"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

class SlowResourcesPage:
    def __init__(self, driver):
        self.driver = driver

    slow_LinkText = (By.XPATH, "//a[text()='Slow Resources']")
    slow_Header = (By.XPATH, "//h3[text()='Slow Resources']")

    # todo - request path
    slow_Request = (By.XPATH, " ")


    def slowResources_Link(self):
        return self.driver.find_element(*SlowResourcesPage.slow_LinkText)

    def slowResources_HeaderText(self):
        return self.driver.find_element(*SlowResourcesPage.slow_Header)

    def slowResources_Request(self):
        return self.driver.find_element(*SlowResourcesPage.slow_Request)


