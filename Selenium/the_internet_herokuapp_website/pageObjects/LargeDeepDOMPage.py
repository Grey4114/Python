"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

class LargeDeepDOMPage:
    def __init__(self, driver):
        self.driver = driver

    largeDeep_LinkText = (By.XPATH, "//a[text()='Large & Deep DOM']")
    largeDeep_Header = (By.XPATH, "//h3[text()='Large & Deep DOM']")

    # todo - scroll down path
    largeDeep_Down = (By.XPATH, " ")

    # todo - scroll across path
    largeDeep_Across = (By.XPATH, " ")

    # todo - table last number
    largeDeep_LastNumber = (By.XPATH, " ")


    def largeDeepDOM_Link(self):
        return self.driver.find_element(*LargeDeepDOMPage.largeDeep_LinkText)

    def largeDeepDOM_HeaderText(self):
        return self.driver.find_element(*LargeDeepDOMPage.largeDeep_Header)

    def largeDeepDOM_ScrollDown(self):
        return self.driver.find_element(*LargeDeepDOMPage.largeDeep_Down)

    def largeDeepDOM_ScrollAcross(self):
        return self.driver.find_element(*LargeDeepDOMPage.largeDeep_Across)

    def largeDeepDOM_TablesLastNumber(self):
        return self.driver.find_element(*LargeDeepDOMPage.largeDeep_LastNumber)




