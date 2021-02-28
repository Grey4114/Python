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

    slow_Link = (By.XPATH, "//a[text()='Slow Resources']")      # Main Page link
    slow_Header = (By.XPATH, "//h3[text()='Slow Resources']")       # Page header text

    # todo - not sure how to test this

    slow_Request = (By.XPATH, " ")      # todo - request path


    def slowResources_LinkText(self):
        return self.driver.find_element(*SlowResourcesPage.slow_Link)

    def slowResources_HeaderText(self):
        return self.driver.find_element(*SlowResourcesPage.slow_Header)

    def slowResources_Request(self):
        return self.driver.find_element(*SlowResourcesPage.slow_Request)


