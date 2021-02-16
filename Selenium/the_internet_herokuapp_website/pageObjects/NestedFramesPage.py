"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - Nested Frames


class NestedFramesPage:
    def __init__(self, driver):
        self.driver = driver

    nested_LinkText = (By.XPATH, "//a[text()='Nested Frames']")

    def nestedFrames_Link(self):
        return self.driver.find_element(*NestedFramesPage.nested_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='Nested Frames']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """
