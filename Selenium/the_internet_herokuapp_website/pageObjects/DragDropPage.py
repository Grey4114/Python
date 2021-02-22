"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Drag and Drop page
"""

from selenium.webdriver.common.by import By

class DragDropPage:
    def __init__(self, driver):
        self.driver = driver

    drag_LinkText = (By.XPATH, "//a[text()='Drag and Drop']")
    drag_Header = (By.XPATH, "//h3[text()='Drag and Drop']")

    # todo - Box A path
    drag_BoxA = (By.XPATH, "")

    # todo - Box B path
    drag_BoxB = (By.XPATH, "")


    def dragDrop_Link(self):
        return self.driver.find_element(*DragDropPage.drag_LinkText)

    def dragDrop_HeaderText(self):
        return self.driver.find_element(*DragDropPage.drag_Header)

    def dragDrop_Box_A(self):
        return self.driver.find_element(*DragDropPage.drag_BoxA)

    def dragDrop_Box(self):
        return self.driver.find_element(*DragDropPage.drag_BoxB)



