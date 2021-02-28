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

    onloadEvent_Link = (By.XPATH, "//a[text()='JavaScript onload event error']")        # Main Page link
    onloadEvent_Text = (By.XPATH, "//h3[text()='JavaScript onload event error']")       # Page header text

    # todo - not sure how to preform this test

    def js_onloadEventError_LinkText(self):
        return self.driver.find_element(*JavaScriptOnloadEventErrorPage.onloadEvent_Link)

    def js_onloadEventError_PageText(self):
        return self.driver.find_element(*JavaScriptOnloadEventErrorPage.onloadEvent_Text)
