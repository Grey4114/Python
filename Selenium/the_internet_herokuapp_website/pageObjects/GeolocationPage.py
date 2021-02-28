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

    geo_Link = (By.XPATH, "//a[text()='Geolocation']")                  # Main Page link
    geo_Header = (By.XPATH, "//h3[text()='Geolocation']")               # Page header text

    geo_WhereAmI = (By.XPATH, "//button[@onclick='getLocation()']")     # Where am i? Button
    geo_Latitude = (By.ID, "lat-value")                                 # Latitude info
    geo_Longtitude = (By.ID, "long-value")                              # Longtitude info
    geo_GLink = (By.XPATH, "//a[text()='See it on Google']")            # Google link text
    geo_GPage = (By.XPATH, "//span[@jstcache='177']")              # Google page


    def geolocation_LinkText(self):
        return self.driver.find_element(*GeolocationPage.geo_Link)

    def geolocation_HeaderText(self):
        return self.driver.find_element(*GeolocationPage.geo_Header)

    def geolocation_WhereAmI_Button(self):
        return self.driver.find_element(*GeolocationPage.geo_WhereAmI)

    def geolocation_LatitudeText(self):
        return self.driver.find_element(*GeolocationPage.geo_Latitude)

    def geolocation_LongtitudeText(self):
        return self.driver.find_element(*GeolocationPage.geo_Longtitude)

    def geolocation_GoogleLink(self):
        return self.driver.find_element(*GeolocationPage.geo_GLink)

    def geolocation_GooglePage(self):
        return self.driver.find_element(*GeolocationPage.geo_GPage)

