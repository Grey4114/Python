"""
Website:  https://the-internet.herokuapp.com/javascript_error
Created:  2/15/2021
Notes:
    Connected Test Object Script - /tests/test_Page_JavaScriptOnloadEventError.py
"""


from selenium.webdriver.common.by import By


class JavaScriptOnloadEventErrorPage:
    def __init__(self, driver):
        self.driver = driver

    onloadEvent_Link = (By.XPATH, "//a[text()='JavaScript onload event error']")        # Main Page link

    def js_onloadEventError_LinkText(self):
        return self.driver.find_element(*JavaScriptOnloadEventErrorPage.onloadEvent_Link)

