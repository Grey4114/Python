"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Checkboxes page
"""

from selenium.webdriver.common.by import By


# todo - break function into separate script page object
# todo - verify being on page


class CheckboxesPage:
    def __init__(self, driver):
        self.driver = driver

    check_LinkText = (By.XPATH, "//a[text()='Checkboxes']")
    checkbox = (By.XPATH, "//input[@type='checkbox']")


    def checkboxes_Link(self):
        return self.driver.find_element(*CheckboxesPage.check_LinkText)

    def checkboxItem(self):
        return self.driver.find_elements(*CheckboxesPage.checkbox)



    """    
    driver.find_element(By.XPATH, "//a[text()='Checkboxes']").click()
    checkBoxs = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    for box in checkBoxs:
        time.sleep(1)
        box.click()

    time.sleep(2)
    driver.back()
    driver.refresh()
    time.sleep(2)
    """


