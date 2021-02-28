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

    hover_Link = (By.XPATH, "//a[text()='Hovers']")     # Main Page link
    hover_Header = (By.XPATH, "//h3[text()='Hovers']")      # Page header text


    hover_Picture1 = (By.XPATH, "//a[@href='/users/1']")        # Pictue 1

    hover_Page1 = (By.XPATH, " ")       # todo - page 1 path


    hover_Picture2 = (By.XPATH, "//a[@href='/users/2']")        # Pictue 2

    hover_Page2 = (By.XPATH, " ")       # todo - page 2 path


    hover_Picture3 = (By.XPATH, "//a[@href='/users/3']")        # Pictue 3

    hover_Page3 = (By.XPATH, " ")       # todo - page 3 path



    def hovers_LinkText(self):
        return self.driver.find_element(*HoversPage.hover_Link)

    def hovers_HeaderText(self):
        return self.driver.find_element(*HoversPage.hover_Header)

    def hovers_Picture_1(self):
        return self.driver.find_element(*HoversPage.hover_Picture1)

    def hovers_WebPage_1(self):
        return self.driver.find_element(*HoversPage.hover_Page1)


    def hovers_Picture_2(self):
        return self.driver.find_element(*HoversPage.hover_Picture2)

    def hovers_WebPage_2(self):
        return self.driver.find_element(*HoversPage.hover_Page2)


    def hovers_Picture_3(self):
        return self.driver.find_element(*HoversPage.hover_Picture3)

    def hovers_WebPage_3(self):
        return self.driver.find_element(*HoversPage.hover_Page3)
