"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


class JavaScriptOnloadEventErrorPage:
    def __init__(self, driver):
        self.driver = driver

    onloadEvent_LinkText = (By.XPATH, "//a[text()='JavaScript onload event error']")
    onloadEvent_Text = (By.XPATH, "//h3[text()='JavaScript onload event error']")


    def js_onloadEventError_Link(self):
        return self.driver.find_element(*JavaScriptOnloadEventErrorPage.onloadEvent_LinkText)

    def js_onloadEventError_PageText(self):
        return self.driver.find_element(*JavaScriptOnloadEventErrorPage.onloadEvent_Text)
