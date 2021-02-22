"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


class HoversPage:
    def __init__(self, driver):
        self.driver = driver

    hover_LinkText = (By.XPATH, "//a[text()='Hovers']")
    hover_Header = (By.XPATH, "//h3[text()='Hovers']")

    # todo - pictue 1 path
    hover_Picture1 = (By.XPATH, " ")
    # todo - name 1 path
    hover_Name1 = (By.XPATH, " ")
    # todo - view 1 path
    hover_View1 = (By.XPATH, " ")
    # todo - page 1 path
    hover_Page1 = (By.XPATH, " ")

    # todo - pictue 2 path
    hover_Picture2 = (By.XPATH, " ")
    # todo - name 2 path
    hover_Name2 = (By.XPATH, " ")
    # todo - view 2 path
    hover_View2 = (By.XPATH, " ")
    # todo - page 2 path
    hover_Page2 = (By.XPATH, " ")

    # todo - pictue 3 path
    hover_Picture3 = (By.XPATH, " ")
    # todo - name 2 path
    hover_Name3 = (By.XPATH, " ")
    # todo - view 2 path
    hover_View3 = (By.XPATH, " ")
    # todo - page 3 path
    hover_Page3 = (By.XPATH, " ")



    def hovers_Link(self):
        return self.driver.find_element(*HoversPage.hover_LinkText)

    def hovers_HeaderText(self):
        return self.driver.find_element(*HoversPage.hover_Header)

    def hovers_Picture_1(self):
        return self.driver.find_element(*HoversPage.hover_Picture1)

    def hovers_UserName_1(self):
        return self.driver.find_element(*HoversPage.hover_Name1)

    def hovers_ViewProfile_1(self):
        return self.driver.find_element(*HoversPage.hover_View1)

    def hovers_WebPage_1(self):
        return self.driver.find_element(*HoversPage.hover_Page1)


    def hovers_Picture_2(self):
        return self.driver.find_element(*HoversPage.hover_Picture2)

    def hovers_UserName_2(self):
        return self.driver.find_element(*HoversPage.hover_Name2)

    def hovers_ViewProfile_2(self):
        return self.driver.find_element(*HoversPage.hover_View2)

    def hovers_WebPage_2(self):
        return self.driver.find_element(*HoversPage.hover_Page2)


    def hovers_Picture_3(self):
        return self.driver.find_element(*HoversPage.hover_Picture3)

    def hovers_UserName_3(self):
        return self.driver.find_element(*HoversPage.hover_Name3)

    def hovers_ViewProfile_3(self):
        return self.driver.find_element(*HoversPage.hover_View3)

    def hovers_WebPage_3(self):
        return self.driver.find_element(*HoversPage.hover_Page3)
