"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""

from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - ForgotPassword


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver

    password_LinkText = (By.XPATH, "//a[text()='Forgot Password']")

    def password_Link(self):
        return self.driver.find_element(*ForgotPasswordPage.password_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='Forgot Password']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """
