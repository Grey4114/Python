"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

class HorizontalSliderPage:
    def __init__(self, driver):
        self.driver = driver

    horizontal_LinkText = (By.XPATH, "//a[text()='Horizontal Slider']")
    horizontal_Header = (By.XPATH, "//h3[text()='Horizontal Slider']")

    # todo - slider path
    horizontal_Slider = (By.XPATH, " ")


    def horizontalSlider_Link(self):
        return self.driver.find_element(*HorizontalSliderPage.horizontal_LinkText)

    def horizontalSlider_HeaderText(self):
        return self.driver.find_element(*HorizontalSliderPage.horizontal_Header)

    def horizontalSlider_Slider(self):
        return self.driver.find_element(*HorizontalSliderPage.horizontal_Slider)

