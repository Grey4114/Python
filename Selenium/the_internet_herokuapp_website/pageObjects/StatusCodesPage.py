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

    status_LinkText = (By.XPATH, "//a[text()='Status Codes']")
    status_Header = (By.XPATH, "//h3[text()='Status Codes']")

    # todo - 200
    status_200 = (By.XPATH, " ")

    # todo - 301
    status_301 = (By.XPATH, " ")

    # todo - 404
    status_404 = (By.XPATH, " ")

    # todo - 500
    status_500 = (By.XPATH, " ")


    def statusCodes_Link(self):
        return self.driver.find_element(*StatusCodesPage.status_LinkText)

    def statusCodes_HeaderText(self):
        return self.driver.find_element(*StatusCodesPage.status_Header)

    def statusCodes_Code200(self):
        return self.driver.find_element(*StatusCodesPage.status_200)

    def statusCodes_Code301(self):
        return self.driver.find_element(*StatusCodesPage.status_301)

    def statusCodes_Code404(self):
        return self.driver.find_element(*StatusCodesPage.status_404)

    def statusCodes_Code500(self):
        return self.driver.find_element(*StatusCodesPage.status_500)



