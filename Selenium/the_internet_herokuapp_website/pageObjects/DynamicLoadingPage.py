"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Dynamic Loading page
"""

from selenium.webdriver.common.by import By

class DynamicLoadingPage:
    def __init__(self, driver):
        self.driver = driver

    loading_LinkText = (By.XPATH, "//a[text()='Dynamic Loading']")
    loading_Header = (By.XPATH, "//h3[text()='Dynamically Loaded Page Elements']")

    # todo - Link1 path
    loading_Ex_Link1 = (By.XPATH, "")
    # todo - Text1 path
    loading_Text1 = (By.XPATH, "")
    # todo - Start1 path
    loading_Start1 = (By.XPATH, "")
    # todo - Hello1 path
    loading_Hello1 = (By.XPATH, "")

    # todo - Link2 path
    loading_Ex_Link2 = (By.XPATH, "")
    # todo - Text2 path
    loading_Text2 = (By.XPATH, "")
    # todo - Start2 path
    loading_Start2 = (By.XPATH, "")
    # todo - Hello2 path
    loading_Hello2 = (By.XPATH, "")


    def dynamicLoading_Link(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_LinkText)

    def dynamicLoading_HeaderText(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Header)



    def dynamicLoading_ExampleLink_1(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Ex_Link1)

    def dynamicLoading_ExampleText_1(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Text1)

    def dynamicLoading_ExampleStart_1(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Start1)

    def dynamicLoading_ExampleHello_1(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Hello1)



    def dynamicLoading_ExampleLink_2(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Ex_Link2)

    def dynamicLoading_ExampleText_2(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Text2)

    def dynamicLoading_ExampleStart_2(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Start2)

    def dynamicLoading_ExampleHello_2(self):
        return self.driver.find_element(*DynamicLoadingPage.loading_Hello2)


    