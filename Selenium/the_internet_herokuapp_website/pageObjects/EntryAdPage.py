"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Dynamic Loading page
"""

from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - the Entry Ad


class EntryAdPage:
    def __init__(self, driver):
        self.driver = driver

    entry_LinkText = (By.XPATH, "//a[text()='Entry Ad']")


    def entryAd_Link(self):
        return self.driver.find_element(*EntryAdPage.entry_LinkText)


    """        
    driver.find_element(By.XPATH, "//a[text()='Entry Ad']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    
    """
