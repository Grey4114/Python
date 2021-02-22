"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


class JQueryUIMenusPage:
    def __init__(self, driver):
        self.driver = driver

    jquery_LinkText = (By.XPATH, "//a[text()='JQuery UI Menus']")
    jquery_Header = (By.XPATH, "//h3[text()='JQueryUI-Menu']")

    # todo - Disabled path
    jquery_Disabled = (By.XPATH, " ")

    # todo - Enabled download pdf path
    jquery_DownPDF = (By.XPATH, " ")

    # todo - Enabled download csv path
    jquery_DownCSV = (By.XPATH, " ")

    # todo - Enabled download xml path
    jquery_DownXML = (By.XPATH, " ")

    # todo - Enabled back path
    jquery_Back = (By.XPATH, " ")

    # todo - Enabled back header path
    jquery_BackHeader = (By.XPATH, " ")

    # todo - Enabled back > Menu path
    jquery_BackMenu = (By.XPATH, " ")



    def jQueryUIMenus_Link(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_LinkText)

    def jQueryUIMenus_HeaderText(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_Header)

    def jQueryUIMenus_Disabled(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_Disabled)

    def jQueryUIMenus_Downloads_PDF(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_DownPDF)

    def jQueryUIMenus_Downloads_CSV(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_DownCSV)

    def jQueryUIMenus_Downloads_XML(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_DownXML)

    def jQueryUIMenus_Back(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_Back)

    def jQueryUIMenus_Back_HeaderText(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_BackHeader)

    def jQueryUIMenus_Back_Menu(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_BackMenu)



