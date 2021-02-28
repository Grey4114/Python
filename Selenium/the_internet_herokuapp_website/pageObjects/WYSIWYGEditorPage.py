"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

class WYSIWYGEditorPage:
    def __init__(self, driver):
        self.driver = driver

    wysiwyg_Link = (By.XPATH, "//a[text()='WYSIWYG Editor']")       # Main Page link
    wysiwyg_Header = (By.XPATH, "//h3[text()='An iFrame containing the TinyMCE WYSIWYG Editor']")    # Page header text

    wysiwyg_iFrame = (By.TAG_NAME, "iframe")  # iFrame location
    wysiwyg_Area = (By.XPATH, "/html/body/p")  # iFrame Text Area


    def WYSIWYGEditor_LinkText(self):
        return self.driver.find_element(*WYSIWYGEditorPage.wysiwyg_Link)

    def WYSIWYGEditor_HeaderText(self):
        return self.driver.find_element(*WYSIWYGEditorPage.wysiwyg_Header)

    def WYSIWYGEditor_iFrame(self):
        return self.driver.find_element(*WYSIWYGEditorPage.wysiwyg_iFrame)

    def WYSIWYGEditor_Area(self):
        return self.driver.find_element(*WYSIWYGEditorPage.wysiwyg_Area)


