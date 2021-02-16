"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - Slow Resources


class SlowResourcesPage:
    def __init__(self, driver):
        self.driver = driver

    slow_LinkText = (By.XPATH, "//a[text()='Slow Resources']")

    def slowResources_Link(self):
        return self.driver.find_element(*SlowResourcesPage.slow_LinkText)


    """    
    driver.find_element(By.XPATH, "//a[text()='Slow Resources']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """
