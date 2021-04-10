"""
Website:  https://the-internet.herokuapp.com/typos
Created:  2/15/2021
Notes:
    Connected Test Object Script - /tests/test_Page_Typos.py
"""


from selenium.webdriver.common.by import By


class TyposPage:
    def __init__(self, driver):
        self.driver = driver


    typos_Link = (By.XPATH, "//a[text()='Typos']")          # Main Page link
    typos_Header = (By.XPATH, "//h3[text()='Typos']")       # Page header text
    typos_Page = (By.TAG_NAME, "body")                      # Get all the text in the page


    def typos_LinkText(self):
        return self.driver.find_element(*TyposPage.typos_Link)

    def typos_HeaderText(self):
        return self.driver.find_element(*TyposPage.typos_Header)

    def typos_PageText(self):
        return self.driver.find_element(*TyposPage.typos_Page)




