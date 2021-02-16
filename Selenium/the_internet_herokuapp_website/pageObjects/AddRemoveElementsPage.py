"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Add Remove Elements page
"""

from selenium.webdriver.common.by import By


# todo - break function into separate script page object
# todo - verify being on page


class AddRemoveElementsPage:
    def __init__(self, driver):
        self.driver = driver

    addremove_LinkText = (By.XPATH, "//a[text()='Add/Remove Elements']")
    addButton = (By.XPATH, "//button[@onclick='addElement()']")
    delButtons = (By.XPATH, "//div[@id='elements']/button[@class='added-manually']")


    def addRemove_Link(self):
        return self.driver.find_element(*AddRemoveElementsPage.addremove_LinkText)


    def addElement(self):
        return self.driver.find_element(*AddRemoveElementsPage.addButton)


    def delElements(self):
        return self.driver.find_elements(*AddRemoveElementsPage.delButtons)


    """            
    time.sleep(2)

    # Click Add Element twice to add 2 delete buttons
    driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()
    driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()
    time.sleep(2)

    # Remove delete buttons
    delButtons = driver.find_elements(By.XPATH, "//div[@id='elements']/button[@class='added-manually']")
    time.sleep(2)

    for button in delButtons:
        button.click()
        time.sleep(1)

    driver.back()
    driver.refresh()
    time.sleep(2)
    """