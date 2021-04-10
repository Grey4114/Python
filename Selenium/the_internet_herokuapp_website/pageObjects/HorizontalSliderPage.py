"""
Website:  https://the-internet.herokuapp.com/horizontal_slider
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_HorizontalSlider.py
"""

from selenium.webdriver.common.by import By

class HorizontalSliderPage:
    def __init__(self, driver):
        self.driver = driver

    horizontal_Link = (By.XPATH, "//a[text()='Horizontal Slider']")         # Main Page link
    horizontal_Header = (By.XPATH, "//h3[text()='Horizontal Slider']")      # Page header text
    horizontal_Slider = (By.XPATH, "//input[@type='range']")                # Slider path
    horizontal_Value = (By.XPATH, "//span[@id='range']")                # Slider value


    def horizontalSlider_LinkText(self):
        return self.driver.find_element(*HorizontalSliderPage.horizontal_Link)

    def horizontalSlider_HeaderText(self):
        return self.driver.find_element(*HorizontalSliderPage.horizontal_Header)

    def horizontalSlider_Slider(self):
        return self.driver.find_element(*HorizontalSliderPage.horizontal_Slider)

    def horizontalSlider_SliderValue(self):
        return self.driver.find_element(*HorizontalSliderPage.horizontal_Value)