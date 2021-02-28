"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


class FramesPage:
    def __init__(self, driver):
        self.driver = driver

    frames_Link = (By.XPATH, "//a[text()='Frames']")        # Main Page link
    frames_Header = (By.XPATH, "//h3[text()='Frames']")         # Page header text


    frames_Nested = (By.XPATH, " ")         # todo - nested link path

    frames_NText = (By.XPATH, " ")          # todo - nested text path

    frames_NRight = (By.XPATH, " ")         # todo - nested right path

    frames_NLeft = (By.XPATH, " ")          # todo - nested left path

    frames_NBottom = (By.XPATH, " ")        # todo - nested bottom path

    frames_iFrame = (By.XPATH, " ")         # todo - iframe text path

    frames_iHeading = (By.XPATH, " ")       # todo - iframe heading path

    frames_iArea = (By.XPATH, " ")          # todo - iframe area path

    # todo - iFrame add all other parameters



    def frames_LinkText(self):
        return self.driver.find_element(*FramesPage.frames_Link)

    def frames_HeaderText(self):
        return self.driver.find_element(*FramesPage.frames_Header)

    def frames_NestedLink(self):
        return self.driver.find_element(*FramesPage.frames_Nested)

    def frames_NestedText(self):
        return self.driver.find_element(*FramesPage.frames_NText)

    def frames_NestedRight(self):
        return self.driver.find_element(*FramesPage.frames_NRight)

    def frames_NestedLeft(self):
        return self.driver.find_element(*FramesPage.frames_NLeft)

    def frames_NestedBottom(self):
        return self.driver.find_element(*FramesPage.frames_NBottom)

    def frames_iFrameLink(self):
        return self.driver.find_element(*FramesPage.frames_iFrame)

    def frames_iFrameHeading(self):
        return self.driver.find_element(*FramesPage.frames_iHeading)

    def frames_iFrameArea(self):
        return self.driver.find_element(*FramesPage.frames_iArea)



