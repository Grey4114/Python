"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Add Remove Elements page
"""

from selenium.webdriver.common.by import By


class AddRemoveElementsPage:
    def __init__(self, driver):
        self.driver = driver

    addremove_Link = (By.XPATH, "//a[text()='Add/Remove Elements']")                    # Main Website link to page
    addremove_Header = (By.XPATH, "//h3[text()='Add/Remove Elements']")                 # Page header text
    addButton = (By.XPATH, "//button[@onclick='addElement()']")                         # Add button
    delButtons = (By.XPATH, "//div[@id='elements']/button[@class='added-manually']")    # Delete button


    def addRemove_LinkText(self):
        return self.driver.find_element(*AddRemoveElementsPage.addremove_Link)

    def addremove_HeaderText(self):
        return self.driver.find_element(*AddRemoveElementsPage.addremove_Header)

    def addElement(self):
        return self.driver.find_element(*AddRemoveElementsPage.addButton)

    def delElements(self):
        return self.driver.find_elements(*AddRemoveElementsPage.delButtons)



