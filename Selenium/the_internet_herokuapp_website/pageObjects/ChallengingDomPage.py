"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Challenging Dom page
"""

from selenium.webdriver.common.by import By


# todo - break function into separate script page object
# todo - verify being on page
# todo - Button 1 and verify
# todo - Button 2 and verify
# todo - Button 3 and verify
# todo - Verify code change


class ChallengingDomPage:
    def __init__(self, driver):
        self.driver = driver

    challenging_LinkText = (By.XPATH, "//a[text()='Challenging DOM']")


    def challengingDom_Link(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='Challenging DOM']").click()
    time.sleep(2)
    driver.back()
    driver.refresh()
    time.sleep(2)
    """

