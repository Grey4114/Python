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

    controls_LinkText = (By.XPATH, "//a[text()='Dynamic Controls']")
    controls_Header = (By.XPATH, "//h3[text()='Dynamic Controls']")

    # todo - checkbox path
    controls_Checkbox = (By.XPATH, "")
    # todo - AddRemove path
    controls_AddRemove = (By.XPATH, "")
    # todo - AddText path
    controls_AddText = (By.XPATH, "")
    # todo - RemoveText path
    controls_RemoveText = (By.XPATH, "")

    # todo - TextField path
    controls_TextField = (By.XPATH, "")
    # todo - Enable path
    controls_Enable = (By.XPATH, "")
    # todo - EnableText path
    controls_EnableText = (By.XPATH, "")
    # todo - DisableText path
    controls_DisableText = (By.XPATH, "")



    def dynamicControls_Link(self):
        return self.driver.find_element(*DynamicControlsPage.controls_LinkText)

    def dynamicControls_HeaderText(self):
        return self.driver.find_element(*DynamicControlsPage.controls_Header)

    def dynamicControls_Checkbox(self):
        return self.driver.find_element(*DynamicControlsPage.controls_Checkbox)

    def dynamicControls_AddRemove(self):
        return self.driver.find_element(*DynamicControlsPage.controls_AddRemove)

    def dynamicControls_AddText(self):
        return self.driver.find_element(*DynamicControlsPage.controls_AddText)

    def dynamicControls_RemoveText(self):
        return self.driver.find_element(*DynamicControlsPage.controls_RemoveText)

    def dynamicControls_TextField(self):
        return self.driver.find_element(*DynamicControlsPage.controls_TextField)

    def dynamicControls_Enable(self):
        return self.driver.find_element(*DynamicControlsPage.controls_Enable)

    def dynamicControls_EnableText(self):
        return self.driver.find_element(*DynamicControlsPage.controls_EnableText)

    def dynamicControls_DisableText(self):
        return self.driver.find_element(*DynamicControlsPage.controls_DisableText)

