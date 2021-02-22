"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Challenging Dom page
"""

from selenium.webdriver.common.by import By

# todo - Blue Button
# todo - Red Button
# todo - Green Button
# todo - Answer Change

class ChallengingDomPage:
    def __init__(self, driver):
        self.driver = driver

    challenging_LinkText = (By.XPATH, "//a[text()='Challenging DOM']")
    challenging_Header = (By.XPATH, "//h3[text()='Challenging DOM']")



    challenging_Blue = (By.XPATH, "//h3[text()='Challenging DOM']")
    challenging_Red = (By.XPATH, "//h3[text()='Challenging DOM']")
    challenging_Green = (By.XPATH, "//h3[text()='Challenging DOM']")
    challenging_Answer = (By.XPATH, "//h3[text()='Challenging DOM']")



    def challengingDom_Link(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_LinkText)

    def challengingDom_HeaderText(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_Header)

    def challengingButton_Blue(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_Blue)

    def challengingButton_Red(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_Red)

    def challengingButton_Green(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_Green)

    def challengingAnswer(self):
        return self.driver.find_element(*ChallengingDomPage.challenging_Answer)


