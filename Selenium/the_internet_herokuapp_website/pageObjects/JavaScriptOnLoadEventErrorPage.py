"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


# todo - break function into separate script page object
# todo - verify being on page
# todo - Java Script Onload Event Error


class JavaScriptOnloadEventErrorPage:
    def __init__(self, driver):
        self.driver = driver

    js_OnloadEvent_LinkText = (By.XPATH, "//a[text()='JavaScript onload event error']")

    def js_onloadEventError_Link(self):
        return self.driver.find_element(*JavaScriptOnloadEventErrorPage.js_OnloadEvent_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='JavaScript onload event error']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """
