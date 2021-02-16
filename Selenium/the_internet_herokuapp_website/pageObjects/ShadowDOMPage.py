"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - Shadow Dom



class ShadowDOMPage:
    def __init__(self, driver):
        self.driver = driver

    shadow_LinkText = (By.XPATH, "//a[text()='Shadow DOM']")

    def shadowDOM_Link(self):
        return self.driver.find_element(*ShadowDOMPage.shadow_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='Shadow DOM']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """
