"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Dynamic Loading page
"""

from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - the dynamic loading


class DynamicLoadingPage:
    def __init__(self, driver):
        self.driver = driver

    loading_LinkText = (By.XPATH, "//a[text()='Dynamic Loading']")


    def dynamicLoading_Link(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='Dynamic Loading']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    
    """

    