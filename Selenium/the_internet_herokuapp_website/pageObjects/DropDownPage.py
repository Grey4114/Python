"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Drop Down page
"""

from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - check the drop downs


class DropDownPage:
    def __init__(self, driver):
        self.driver = driver

    drop_LinkText = (By.XPATH, "//a[text()='Dropdown']")

    def dropdown_Link(self):
        return self.driver.find_element(*DropDownPage.drop_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='Dropdown']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """
