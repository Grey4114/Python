"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""

from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - Floating menu



class FloatingMenuPage:
    def __init__(self, driver):
        self.driver = driver

    floating_LinkText = (By.XPATH, "//a[text()='Floating Menu']")


    def floating_Link(self):
        return self.driver.find_element(*FloatingMenuPage.floating_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='Floating Menu']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)

    """