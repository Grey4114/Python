"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""

from selenium.webdriver.common.by import By

class GeolocationPage:
    def __init__(self, driver):
        self.driver = driver

    geo_LinkText = (By.XPATH, "//a[text()='Geolocation']")
    geo_Header = (By.XPATH, "//h3[text()='Geolocation']")

    # todo - where am i path
    geo_WhereAmI = (By.XPATH, " ")
    # todo - latitude path
    geo_Latitude = (By.XPATH, " ")
    # todo - longtitude path
    geo_Longtitude = (By.XPATH, " ")
    # todo - google link path
    geo_GLink = (By.XPATH, " ")
    # todo - google page path
    geo_GPage = (By.XPATH, " ")


    def geolocation_Link(self):
        return self.driver.find_element(*GeolocationPage.geo_LinkText)

    def geolocation_HeaderText(self):
        return self.driver.find_element(*GeolocationPage.geo_LinkText)

    def geolocation_WhereAmI_Button(self):
        return self.driver.find_element(*GeolocationPage.geo_WhereAmI)

    def geolocation_Latitude_Text(self):
        return self.driver.find_element(*GeolocationPage.geo_Latitude)

    def geolocation_Longtitude_Text(self):
        return self.driver.find_element(*GeolocationPage.geo_Longtitude)

    def geolocation_GoogleLink(self):
        return self.driver.find_element(*GeolocationPage.geo_GLink)

    def geolocation_GooglePage(self):
        return self.driver.find_element(*GeolocationPage.geo_GPage)

