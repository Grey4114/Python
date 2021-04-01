"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Challenging Dom page
"""

from selenium.webdriver.common.by import By

class ChallengingDomPage:
    def __init__(self, driver):
        self.driver = driver

    challenging_Link = (By.XPATH, "//a[text()='Challenging DOM']")          # Main Page link
    challenging_Header = (By.XPATH, "//h3[text()='Challenging DOM']")       # Page header text

    challenging_Blue = (By.XPATH, "//a[@class='button']")                   # Blue Button
    challenging_Red = (By.XPATH, "//a[@class='button alert']")              # Red Button
    challenging_Green = (By.XPATH, "//a[@class='button success']")          # Green Button

    challenging_Canvas = (By.XPATH, "//canvas[@id='canvas']")               # Canvas


    def challengingDom_LinkText(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_Link)

    def challengingDom_HeaderText(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_Header)

    def challenging_ButtonBlue(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_Blue)

    def challenging_ButtonRed(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_Red)

    def challenging_ButtonGreen(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_Green)

    def challengingDom_Canvas(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_Canvas)



