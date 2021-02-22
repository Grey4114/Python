"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Broken Images page
"""

from selenium.webdriver.common.by import By

# todo - find a better way to check for broken images

class BrokenImagePage:
    def __init__(self, driver):
        self.driver = driver

    broken_LinkText = (By.XPATH, "//a[text()='Broken Images']")
    broken_Header = (By.XPATH, "//h3[text()='Broken Images']")

    broken_1 = (By.XPATH, "//div[@class='example']/img[@src='asdf.jpg']")
    broken_2 = (By.XPATH, "//div[@class='example']/img[@src='hjkl.jpg']")
    broken_3 = (By.XPATH, "//div[@class='example']/img[@src='img/avatar-blank.jpg']")

    def broken_Link(self):
        return self.driver.find_element(*BrokenImagePage.broken_LinkText)

    def broken_HeaderText(self):
        return self.driver.find_element(*BrokenImagePage.broken_Header)


    def brokenImage_1(self):
        return self.driver.find_element(*BrokenImagePage.broken_1)

    def brokenImage_2(self):
        return self.driver.find_element(*BrokenImagePage.broken_2)

    def brokenImage_3(self):
        return self.driver.find_element(*BrokenImagePage.broken_3)

