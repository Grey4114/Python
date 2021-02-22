"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the ContextMenu page
"""

from selenium.webdriver.common.by import By

# todo - right click box
# todo - dismiss alert box
# todo - dismiss popup box


class ContextMenuPage:
    def __init__(self, driver):
        self.driver = driver

    context_LinkText = (By.XPATH, "//a[text()='Context Menu']")
    context_Header = (By.XPATH, "//h3[text()='Context Menu']")

    context_Right = (By.XPATH, "")
    context_Alert = (By.XPATH, "")
    context_Popup = (By.XPATH, "")


    def contextMenu_Link(self):
        return self.driver.find_element(*ContextMenuPage.context_LinkText)

    def contextMenu_HeaderText(self):
        return self.driver.find_element(*ContextMenuPage.context_Header)



    def contextMenu_RightClickBox(self):
        return self.driver.find_element(*ContextMenuPage.context_Right)

    def contextMenu_AlertBox(self):
        return self.driver.find_element(*ContextMenuPage.context_Alert)

    def contextMenu_PopupBox(self):
        return self.driver.find_element(*ContextMenuPage.context_Popup)
