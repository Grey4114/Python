"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""

from selenium.webdriver.common.by import By


class ShiftingContentPage:
    def __init__(self, driver):
        self.driver = driver

    shifting_Link = (By.XPATH, "//a[text()='Shifting Content']")        # Main Page link
    shifting_Header = (By.XPATH, "//h3[text()='Shifting Content']")     # Page header text

    shifting_Menu = (By.XPATH, "//a[@href='/shifting_content/menu']")     # Menu button
    shifting_Image = (By.XPATH, "//a[@href='/shifting_content/image'] ")        # Image Button
    shifting_List = (By.XPATH, "//a[@href='/shifting_content/list'] ")     # List button

    example1_Header = (By.XPATH, "//h3[text()='Shifting Content: Menu Element']")   # Example 1 - Header
    example1_Random = (By.XPATH, "//a[@href='/shifting_content/menu?mode=random']")     # Click here - random
    example1_Shift = (By.XPATH, "//a[@href='/shifting_content/menu?pixel_shift=100']")     # Click here - shift 100
    example1_RandomShift = (By.XPATH, "//a[@href='/shifting_content/menu?mode=random&pixel_shift=100']")    # Click here - random & shift 100

    example2_Header = (By.XPATH, "//h3[text()='Shifting Content: Image']")       # Example 2 - Header
    example2_Shift = (By.XPATH, "//a[@href='/shifting_content/image?mode=random']")        # Example 2 - shift
    example2_Random = (By.XPATH, "//a[@href='/shifting_content/image?pixel_shift=100']")       # Example 2 - Random
    example2_RandomShift = (By.XPATH, "//a[@href='/shifting_content/image?mode=random&pixel_shift=100']")   # Example 2 - Simple Image
    example2_Simple = (By.XPATH, "//a[@href='/shifting_content/image?image_type=simple']")       # Example 2 - Simple Image

    example2_Image = (By.XPATH, "//img[@src='/img/avatar.jpg']")       # Example 2 - Image
    example2_SimpleImage = (By.XPATH, "//img[@src='/img/avatars/Original-Facebook-Geek-Profile-Avatar-2.jpg']")  # Example 2 - Simple Image


    example3_Header = (By.XPATH, "//h3[text()='Shifting Content: List']")       # Example 3 - Header
    example3_Text = (By.XPATH, "//div[@class='large-6 columns large-centered']")     # Example 3 - Text



    def shiftingContent_LinkText(self):
        return self.driver.find_element(*ShiftingContentPage.shifting_Link)

    def shiftingContent_HeaderText(self):
        return self.driver.find_element(*ShiftingContentPage.shifting_Header)

    def shiftingContent_MenuLink(self):
        return self.driver.find_element(*ShiftingContentPage.shifting_Menu)

    def shiftingContent_ImageLink(self):
        return self.driver.find_element(*ShiftingContentPage.shifting_Image)

    def shiftingContent_ListLink(self):
        return self.driver.find_element(*ShiftingContentPage.shifting_List)



    def shiftingContent_Example1_HeaderText(self):
        return self.driver.find_element(*ShiftingContentPage.example1_Header)

    def shiftingContent_Example1_Shift(self):
        return self.driver.find_element(*ShiftingContentPage.example1_Shift)

    def shiftingContent_Example1_Random(self):
        return self.driver.find_element(*ShiftingContentPage.example1_Random)

    def shiftingContent_Example1_RandomShift(self):
        return self.driver.find_element(*ShiftingContentPage.example1_RandomShift)



    def shiftingContent_Example2_HeaderText(self):
        return self.driver.find_element(*ShiftingContentPage.example2_Header)

    def shiftingContent_Example2_Shift(self):
        return self.driver.find_element(*ShiftingContentPage.example2_Shift)

    def shiftingContent_Example2_Random(self):
        return self.driver.find_element(*ShiftingContentPage.example2_Random)

    def shiftingContent_Example2_Simple(self):
        return self.driver.find_element(*ShiftingContentPage.example2_Simple)



    def shiftingContent_Example3_HeaderText(self):
        return self.driver.find_element(*ShiftingContentPage.example3_Header)

    def shiftingContent_Example3_Text(self):
        return self.driver.find_element(*ShiftingContentPage.example3_Text)

