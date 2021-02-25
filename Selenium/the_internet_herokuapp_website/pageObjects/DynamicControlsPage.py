"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Dynamic Controls page
"""

from selenium.webdriver.common.by import By

class DynamicControlsPage:
    def __init__(self, driver):
        self.driver = driver

    controls_Link = (By.XPATH, "//a[text()='Dynamic Controls']")        # Main Page link
    controls_Header = (By.XPATH, "//h4[text()='Dynamic Controls']")     # Page header text

    controls_Checkbox = (By.XPATH, "//div[@id='checkbox']")                     # Checkbox path
    controls_AddRemove = (By.XPATH, "//button[@onclick='swapCheckbox()']")      # AddRemove button path
    controls_TextField = (By.XPATH, "//input[@type='text']")                    # Text Field path
    controls_Enable = (By.XPATH, "//button[@onclick='swapInput()']")            # Enable/Disabel button path
    controls_Message = (By.XPATH, "//p[@id='message']")                         # Message text used for both buttons


    def dynamicControls_LinkText(self):
        return self.driver.find_element(*DynamicControlsPage.controls_Link)

    def dynamicControls_HeaderText(self):
        return self.driver.find_element(*DynamicControlsPage.controls_Header)

    def dynamicControls_Checkbox(self):
        return self.driver.find_element(*DynamicControlsPage.controls_Checkbox)

    def dynamicControls_AddRemoveButton(self):
        return self.driver.find_element(*DynamicControlsPage.controls_AddRemove)

    def dynamicControls_TextField(self):
        return self.driver.find_element(*DynamicControlsPage.controls_TextField)

    def dynamicControls_EnableDisableButton(self):
        return self.driver.find_element(*DynamicControlsPage.controls_Enable)

    def dynamicControls_MessageText(self):
        return self.driver.find_element(*DynamicControlsPage.controls_Message)

