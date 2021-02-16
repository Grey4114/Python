"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Drag and Drop page
"""

from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - check the drag and drop


class DragDropPage:
    def __init__(self, driver):
        self.driver = driver

    drag_LinkText = (By.XPATH, "//a[text()='Drag and Drop']")


    def dragDrop_Link(self):
        return self.driver.find_element(*DragDropPage.drag_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='Drag and Drop']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    
    """
