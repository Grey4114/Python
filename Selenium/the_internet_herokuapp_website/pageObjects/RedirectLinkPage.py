"""
Website:  https://the-internet.herokuapp.com/redirector
Created:  2/15/2021
Notes:
    Connected Test Object Script - /tests/test_Page_RedirectLink.py
"""


from selenium.webdriver.common.by import By

class RedirectLinkPage:
    def __init__(self, driver):
        self.driver = driver

    redirect_Link = (By.XPATH, "//a[text()='Redirect Link']")       # Main Page link
    redirect_Header = (By.XPATH, "//h3[text()='Redirection']")        # Page header text
    redirect_Click = (By.XPATH, "//a[@href='redirect']")        # Click link



    def redirectLink_LinkText(self):
        return self.driver.find_element(*RedirectLinkPage.redirect_Link)

    def redirectLink_HeaderText(self):
        return self.driver.find_element(*RedirectLinkPage.redirect_Header)

    def redirectLink_ClickHere(self):
        return self.driver.find_element(*RedirectLinkPage.redirect_Click)

