"""
Website:  https://the-internet.herokuapp.com/dynamic_content
Created:  2/14/2021
Notes:
    Connected Test Object Script - /tests/test_Page_DynamicContent.py
"""

from selenium.webdriver.common.by import By

class DynamicContentPage:
    def __init__(self, driver):
        self.driver = driver

    content_Link = (By.XPATH, "//a[text()='Dynamic Content']")          # Main Page link
    content_Header = (By.XPATH, "//h3[text()='Dynamic Content']")       # Page header text
    content_ClickHere = (By.XPATH, "//a[text()='click here']")          # click here path
    content_Images = (By.XPATH, "//div[@class='large-2 columns']/img")  # Three Page Images
    content_Texts = (By.XPATH, "//div[@class='large-10 columns']")      # Three Image Texts


    def dynamicContent_LinkText(self):
        return self.driver.find_element(*DynamicContentPage.content_Link)

    def dynamicContent_HeaderText(self):
        return self.driver.find_element(*DynamicContentPage.content_Header)

    def dynamicContent_ClickHere(self):
        return self.driver.find_element(*DynamicContentPage.content_ClickHere)

    def dynamicContent_PageImages(self):
        return self.driver.find_elements(*DynamicContentPage.content_Images)

    def dynamicContent_PageTexts(self):
        return self.driver.find_elements(*DynamicContentPage.content_Texts)


    # image_1 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-1.jpg"
    # image_2 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-2.jpg"
    # image_3 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg"
    # image_4 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-5.jpg"
    # image_5 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-7.jpg"
