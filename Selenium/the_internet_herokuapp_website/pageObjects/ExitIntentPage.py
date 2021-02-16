"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intentpage
"""

from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - the Exit Intent


class ExitIntentPage:
    def __init__(self, driver):
        self.driver = driver

    exit_LinkText = (By.XPATH, "//a[text()='Exit Intent']")


    def exitIntent_Link(self):
        return self.driver.find_element(*ExitIntentPage.exit_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='Exit Intent']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    
    """