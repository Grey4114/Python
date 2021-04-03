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

    drag_Link = (By.XPATH, "//a[text()='Drag and Drop']")       # Main Page link
    drag_Header = (By.XPATH, "//h3[text()='Drag and Drop']")    # Page header text

    drag_BoxA = (By.ID, "column-a")      # Box A path
    drag_BoxB = (By.ID, "column-b")      # Box B path

    #"div[id='column-b']"

    def dragDrop_LinkText(self):
        return self.driver.find_element(*DragDropPage.drag_Link)

    def dragDrop_HeaderText(self):
        return self.driver.find_element(*DragDropPage.drag_Header)

    def dragDrop_Box_A(self):
        return self.driver.find_element(*DragDropPage.drag_BoxA)

    def dragDrop_Box_B(self):
        return self.driver.find_element(*DragDropPage.drag_BoxB)



