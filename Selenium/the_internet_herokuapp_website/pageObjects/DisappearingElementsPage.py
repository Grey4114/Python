"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Digest Authorization page
"""

from selenium.webdriver.common.by import By


class DisappearingElementsPage:
    def __init__(self, driver):
        self.driver = driver

    disappearing_Link = (By.XPATH, "//a[text()='Disappearing Elements']")       # Main Page link
    disappearing_Header = (By.XPATH, "//h3[text()='Disappearing Elements']")    # Page header text

    disappearing_Home = (By.XPATH, "//a[@href='/']")                     # Home button path
    disappearing_About = (By.XPATH, "//a[@href='/about/']")              # About button path
    disappearing_Contact = (By.XPATH, "//a[@href='/contact-us/']")       # Contact button path
    disappearing_Portfolio = (By.XPATH, "//a[@href='/portfolio/']")      # Portfolio button path
    disappearing_Gallery = (By.XPATH, "//a[@href='/gallery/']")          # Gallery button path


    def disappearingElements_LinkText(self):
        return self.driver.find_element(*DisappearingElementsPage.disappearing_Link)

    def disappearingElements_HeaderText(self):
        return self.driver.find_element(*DisappearingElementsPage.disappearing_Header)

    def disappearingElements_HomeButton(self):
        return self.driver.find_element(*DisappearingElementsPage.disappearing_Home)

    def disappearingElements_AboutButton(self):
        return self.driver.find_element(*DisappearingElementsPage.disappearing_About)

    def disappearingElements_ContactButton(self):
        return self.driver.find_element(*DisappearingElementsPage.disappearing_Contact)

    def disappearingElements_PortfilioButton(self):
        return self.driver.find_element(*DisappearingElementsPage.disappearing_Portfolio)

    def disappearingElements_GalleryButton(self):
        return self.driver.find_element(*DisappearingElementsPage.disappearing_Gallery)

