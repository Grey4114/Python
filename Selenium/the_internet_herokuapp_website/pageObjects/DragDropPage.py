"""
Website:  https://the-internet.herokuapp.com/drag_and_drop
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_DragDrop.py
"""

from selenium.webdriver.common.by import By

class DragDropPage:
    def __init__(self, driver):
        self.driver = driver

    drag_Link = (By.XPATH, "//a[text()='Drag and Drop']")       # Main Page link
    drag_Header = (By.XPATH, "//h3[text()='Drag and Drop']")    # Page header text
    drag_BoxA = (By.CSS_SELECTOR, "#column-a")      # Box A path
    drag_BoxB = (By.CSS_SELECTOR, "#column-b")      # Box B path


    def dragDrop_LinkText(self):
        return self.driver.find_element(*DragDropPage.drag_Link)

    def dragDrop_HeaderText(self):
        return self.driver.find_element(*DragDropPage.drag_Header)

    def dragDrop_Box_A(self):
        return self.driver.find_element(*DragDropPage.drag_BoxA)

    def dragDrop_Box_B(self):
        return self.driver.find_element(*DragDropPage.drag_BoxB)



