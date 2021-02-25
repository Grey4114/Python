"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Broken Images page
"""

from selenium.webdriver.common.by import By

class BrokenImagePage:
    def __init__(self, driver):
        self.driver = driver

    broken_Link = (By.XPATH, "//a[text()='Broken Images']")            # Main Page link
    broken_Header = (By.XPATH, "//h3[text()='Broken Images']")         # Page header text

    broken_Image1 = (By.XPATH, "//div[@class='example']/img[@src='asdf.jpg']")              # Broken Image 1
    broken_Image2 = (By.XPATH, "//div[@class='example']/img[@src='hjkl.jpg']")              # Broken Image 2
    broken_Image3 = (By.XPATH, "//div[@class='example']/img[@src='img/avatar-blank.jpg']")  # Broken Image 3

    def broken_LinkText(self):
        return self.driver.find_element(*BrokenImagePage.broken_Link)

    def broken_HeaderText(self):
        return self.driver.find_element(*BrokenImagePage.broken_Header)

    def brokenImage_1(self):
        return self.driver.find_element(*BrokenImagePage.broken_Image1)

    def brokenImage_2(self):
        return self.driver.find_element(*BrokenImagePage.broken_Image2)

    def brokenImage_3(self):
        return self.driver.find_element(*BrokenImagePage.broken_Image3)

