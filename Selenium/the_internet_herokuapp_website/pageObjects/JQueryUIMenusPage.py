"""
Website:  https://the-internet.herokuapp.com/jqueryui/menu
Created:  2/15/2021
Notes:
    Connected Test Object Script - /tests/test_Page_JQueryUIMenus.py
"""


from selenium.webdriver.common.by import By


class JQueryUIMenusPage:
    def __init__(self, driver):
        self.driver = driver

    jquery_Link = (By.XPATH, "//a[text()='JQuery UI Menus']")           # Main Page link
    jquery_Header = (By.XPATH, "//h3[text()='JQueryUI - Menu']")          # Page header text

    jquery_Enabled = (By.XPATH, "//a[normalize-space()='Downloads']")
    jquery_Downloads = (By.XPATH, "//li[@id='ui-id-4']")
    jquery_PDF = (By.XPATH, "//li[@id='ui-id-5']")
    jquery_CSV = (By.XPATH, "//li[@id='ui-id-6']")
    jquery_XML = (By.XPATH, "//li[@id='ui-id-7']")
    jquery_Back = (By.XPATH, "//li[@id='ui-id-8'] ")


    def jQueryUIMenus_LinkText(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_Link)

    def jQueryUIMenus_HeaderText(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_Header)

    def jQueryUIMenus_EnabledLink(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_Enabled)

    def jQueryUIMenus_Downloads_PDF(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_PDF)

    def jQueryUIMenus_Downloads_CSV(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_CSV)

    def jQueryUIMenus_Downloads_XML(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_XML)

    def jQueryUIMenus_Back(self):
        return self.driver.find_element(*JQueryUIMenusPage.jquery_Back)




