"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

class StatusCodesPage:
    def __init__(self, driver):
        self.driver = driver

    """According to online info there is no way for Selenium to get status codes for a web page"""

    status_Link = (By.XPATH, "//a[text()='Status Codes']")      # Main Page link
    status_Header = (By.XPATH, "//h3[text()='Status Codes']")       # Page header text


    def statusCodes_LinkText(self):
        return self.driver.find_element(*StatusCodesPage.status_Link)

    def statusCodes_HeaderText(self):
        return self.driver.find_element(*StatusCodesPage.status_Header)




