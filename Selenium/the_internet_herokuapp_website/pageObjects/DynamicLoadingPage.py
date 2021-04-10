"""
Website:  https://the-internet.herokuapp.com/dynamic_loading
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_DynamicLoading.py
"""

from selenium.webdriver.common.by import By

class DynamicLoadingPage:
    def __init__(self, driver):
        self.driver = driver

    loading_Link = (By.XPATH, "//a[text()='Dynamic Loading']")                          # Main Page link
    loading_Header = (By.XPATH, "//h3[text()='Dynamically Loaded Page Elements']")      # Page header text
    loading_Example_1 = (By.XPATH, "//a[@href='/dynamic_loading/1']")                   # Example 1 Link path
    loading_Example_2 = (By.XPATH, "//a[@href='/dynamic_loading/2']")                   # Example 2 Link path
    loading_Start1 = (By.XPATH, "//button[text()='Start']")                             # Example 1 Start Button
    loading_Hello1 = (By.XPATH, "//div[@id='finish']")                                  # Example 1 Hidden Hello text
    loading_Start2 = (By.XPATH, "//button[text()='Start']")                             # Example 2 Start Button
    loading_Hello2 = (By.XPATH, "//div[@id='finish']/h4[text()='Hello World!']")        # Example 2 Hidden Hello text


    def dynamicLoading_LinkText(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Link)

    def dynamicLoading_HeaderText(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Header)

    def dynamicLoading_ExampleLink_1(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Example_1)

    def dynamicLoading_ExampleLink_2(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Example_2)

    def dynamicLoading_ExampleStart_1(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Start1)

    def dynamicLoading_ExampleHello_1(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Hello1)

    def dynamicLoading_ExampleStart_2(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Start2)

    def dynamicLoading_ExampleHello_2(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Hello2)


    