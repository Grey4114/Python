"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Broken Images page
"""

from selenium.webdriver.common.by import By


# todo - break function into separate script page object
# todo - verify being on page
# todo - Verify all 3 images


class BrokenImagePage:
    def __init__(self, driver):
        self.driver = driver


    broken_LinkText = (By.XPATH, "//a[text()='Broken Images']")


    def broken_Link(self):
        return self.driver.find_element(*BrokenImagePage.broken_LinkText)


    """        
    driver.find_element(By.XPATH, "//a[text()='Broken Images']").click()
    time.sleep(2)
    driver.back()
    driver.refresh()
    time.sleep(2)

    """