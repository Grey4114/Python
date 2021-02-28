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

    status_Link = (By.XPATH, "//a[text()='Status Codes']")      # Main Page link
    status_Header = (By.XPATH, "//h3[text()='Status Codes']")       # Page header text

    # todo - not sure how to conduct the tests for this page
    status_200 = (By.XPATH, "//a[@href='status_codes/200']")    # Code 200

    status_301 = (By.XPATH, "//a[@href='status_codes/301']")    # Code 301

    status_404 = (By.XPATH, "//a[@href='status_codes/404']")    # Code 404

    status_500 = (By.XPATH, "//a[@href='status_codes/500']")    # Code 500


    def statusCodes_LinkText(self):
        return self.driver.find_element(*StatusCodesPage.status_Link)

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



