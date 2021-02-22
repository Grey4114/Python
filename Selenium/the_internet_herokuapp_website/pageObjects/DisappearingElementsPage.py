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

    disappearing_LinkText = (By.XPATH, "//a[text()='Disappearing Elements']")
    disappearing_Header = (By.XPATH, "//h3[text()='Disappearing Elements']")

    # todo - Home button path
    disappearing_Home = (By.XPATH, "")

    # todo - About button path
    disappearing_About = (By.XPATH, "")

    # todo - Contact button path
    disappearing_Contact = (By.XPATH, "")

    # todo - Portfolio button path
    disappearing_Portfolio = (By.XPATH, "")

    # todo - Gallery button path
    disappearing_Gallery = (By.XPATH, "")




    def disappearingElements_Link(self):
        return self.driver.find_element(*DisappearingElementsPage.disappearing_LinkText)

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

