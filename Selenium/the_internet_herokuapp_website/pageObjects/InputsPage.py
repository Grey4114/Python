"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


class InputsPage:
    def __init__(self, driver):
        self.driver = driver

    inputs_LinkText = (By.XPATH, "//a[text()='Inputs']")
    inputs_Header = (By.XPATH, "//h3[text()='Inputs']")

    # todo - manual path
    inputs_Manual = (By.XPATH, " ")
    # todo - select arrow path
    inputs_Arrows = (By.XPATH, " ")




    def inputs_Link(self):
        return self.driver.find_element(*InputsPage.inputs_LinkText)

    def inputs_HeaderText(self):
        return self.driver.find_element(*InputsPage.inputs_Header)

    def inputs_ManualNumber(self):
        return self.driver.find_element(*InputsPage.inputs_Manual)

    def inputs_SelectArrow(self):
        return self.driver.find_element(*InputsPage.inputs_Arrows)
