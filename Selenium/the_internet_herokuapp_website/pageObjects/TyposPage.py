"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


class TyposPage:
    def __init__(self, driver):
        self.driver = driver

    typos_LinkText = (By.XPATH, "//a[text()='Typos']")
    typos_Header = (By.XPATH, "//h3[text()='Typos']")

    # todo - text 1
    typos_Text1 = (By.XPATH, " ")
    # todo - text 2
    typos_Text2 = (By.XPATH, " ")



    def typos_Link(self):
        return self.driver.find_element(*TyposPage.typos_LinkText)

    def typos_HeaderText(self):
        return self.driver.find_element(*TyposPage.typos_Header)

    def typos_Text_1(self):
        return self.driver.find_element(*TyposPage.typos_Text1)

    def typos_Text_2(self):
        return self.driver.find_element(*TyposPage.typos_Text2)



