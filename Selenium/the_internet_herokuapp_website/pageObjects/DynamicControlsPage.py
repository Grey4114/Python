"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Dynamic Controls page
"""

from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - the dynamic controls


class DynamicContentPage:
    def __init__(self, driver):
        self.driver = driver

    controls_LinkText = (By.XPATH, "//a[text()='Dynamic Controls']")


    def dynamicControls_Link(self):
        return self.driver.find_element(*DynamicContentPage.controls_LinkText)



    """
    driver.find_element(By.XPATH, "//a[text()='Dynamic Controls']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    
    """
