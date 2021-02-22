"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

class MultipleWindowsPage:
    def __init__(self, driver):
        self.driver = driver

    multiple_LinkText = (By.XPATH, "//a[text()='Multiple Windows']")
    multiple_Header = (By.XPATH, "//h3[text()='Multiple Windows']")

    # todo - click here path
    multiple_Click = (By.XPATH, " ")

    # todo - new web page
    multiple_NewPage = (By.XPATH, " ")

    # todo - New page header path
    multiple_NewHeader = (By.XPATH, " ")


    def multipleWindows_Link(self):
        return self.driver.find_element(*MultipleWindowsPage.multiple_LinkText)

    def multipleWindows_HeaderText(self):
        return self.driver.find_element(*MultipleWindowsPage.multiple_Header)

    def multipleWindows_ClickHere(self):
        return self.driver.find_element(*MultipleWindowsPage.multiple_Click)

    def multipleWindows_NewPageURL(self):
        return self.driver.find_element(*MultipleWindowsPage.multiple_NewPage)

    def multipleWindows_NewHeader(self):
        return self.driver.find_element(*MultipleWindowsPage.multiple_NewHeader)


