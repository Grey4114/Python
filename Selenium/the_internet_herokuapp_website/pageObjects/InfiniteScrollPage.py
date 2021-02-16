"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - Infinite Scroll


class InfiniteScrollPage:
    def __init__(self, driver):
        self.driver = driver

    infinite_LinkText = (By.XPATH, "//a[text()='Infinite Scroll']")

    def infiniteScroll_Link(self):
        return self.driver.find_element(*InfiniteScrollPage.infinite_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='Infinite Scroll']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """