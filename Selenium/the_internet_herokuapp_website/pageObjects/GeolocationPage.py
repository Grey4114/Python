"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - Geolocation


class GeolocationPage:
    def __init__(self, driver):
        self.driver = driver

    geo_LinkText = (By.XPATH, "//a[text()='Geolocation']")


    def geolocation_Link(self):
        return self.driver.find_element(*GeolocationPage.geo_LinkText)



    """
    driver.find_element(By.XPATH, "//a[text()='Geolocation']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    
    """
