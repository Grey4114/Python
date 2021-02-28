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

    inputs_Link = (By.XPATH, "//a[text()='Inputs']")    # Main Page link
    inputs_Header = (By.XPATH, "//h3[text()='Inputs']")     # Page header text
    inputs_Number = (By.XPATH, "//input[@type='number']")     # Number field


    def inputs_LinkText(self):
        return self.driver.find_element(*InputsPage.inputs_Link)

    def inputs_HeaderText(self):
        return self.driver.find_element(*InputsPage.inputs_Header)

    def inputs_NumberField(self):
        return self.driver.find_element(*InputsPage.inputs_Number)

