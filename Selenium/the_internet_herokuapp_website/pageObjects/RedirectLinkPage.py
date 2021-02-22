"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

class RedirectLinkPage:
    def __init__(self, driver):
        self.driver = driver

    redirect_LinkText = (By.XPATH, "//a[text()='Redirect Link']")
    redirect_Header = (By.XPATH, "//h3[text()='Redirect Link']")

    # todo - click here path
    redirect_Click = (By.XPATH, " ")

    # todo - New Page path
    redirect_NewPage = (By.XPATH, " ")

    # todo - New Header path
    redirect_NewHeader = (By.XPATH, " ")



    def redirectLink_Link(self):
        return self.driver.find_element(*RedirectLinkPage.redirect_LinkText)

    def redirectLink_HeaderText(self):
        return self.driver.find_element(*RedirectLinkPage.redirect_Header)

    def redirectLink_ClickHere(self):
        return self.driver.find_element(*RedirectLinkPage.redirect_Click)

    def redirectLink_NewPageURL(self):
        return self.driver.find_element(*RedirectLinkPage.redirect_NewPage)

    def redirectLink_NewPageHeader(self):
        return self.driver.find_element(*RedirectLinkPage.redirect_NewHeader)

