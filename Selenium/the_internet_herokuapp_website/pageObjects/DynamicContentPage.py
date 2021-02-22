"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Dynamic Content page
"""

from selenium.webdriver.common.by import By

class DynamicContentPage:
    def __init__(self, driver):
        self.driver = driver

    content_LinkText = (By.XPATH, "//a[text()='Dynamic Content']")
    content_Header = (By.XPATH, "//h3[text()='Dynamic Content']")


    # todo - click here path
    content_ClickHere = (By.XPATH, "")

    # todo - image / text 1 path
    content_Image1 = (By.XPATH, "")
    content_Text1 = (By.XPATH, "")

    # todo - image / text 2 path
    content_Image2 = (By.XPATH, "")
    content_Text2 = (By.XPATH, "")

    # todo - image / text 3A path
    content_Image3A = (By.XPATH, "")
    content_Text3A = (By.XPATH, "")

    # todo - image / text 3B path
    content_Image3B = (By.XPATH, "")
    content_Text3B = (By.XPATH, "")

    # todo - image / text 3C path
    content_Image3C = (By.XPATH, "")
    content_Text3C = (By.XPATH, "")



    def dynamicContent_Link(self):
        return self.driver.find_element(*DynamicContentPage.content_LinkText)

    def dynamicContent_HeaderText(self):
        return self.driver.find_element(*DynamicContentPage.content_Header)

    def dynamicContent_ClickHere(self):
        return self.driver.find_element(*DynamicContentPage.content_ClickHere)

    def dynamicContent_Image_1(self):
        return self.driver.find_element(*DynamicContentPage.content_Image1)

    def dynamicContent_Text_1(self):
        return self.driver.find_element(*DynamicContentPage.content_Text1)

    def dynamicContent_Image_2(self):
        return self.driver.find_element(*DynamicContentPage.content_Image2)

    def dynamicContent_Text_2(self):
        return self.driver.find_element(*DynamicContentPage.content_Text2)

    def dynamicContent_Image_3A(self):
        return self.driver.find_element(*DynamicContentPage.content_Image3A)

    def dynamicContent_Text_3A(self):
        return self.driver.find_element(*DynamicContentPage.content_Text3A)

    def dynamicContent_Image_3B(self):
        return self.driver.find_element(*DynamicContentPage.content_Image3B)

    def dynamicContent_Text_3B(self):
        return self.driver.find_element(*DynamicContentPage.content_Text3B)

    def dynamicContent_Image_3C(self):
        return self.driver.find_element(*DynamicContentPage.content_Image3C)

    def dynamicContent_Text_3C(self):
        return self.driver.find_element(*DynamicContentPage.content_Text3C)