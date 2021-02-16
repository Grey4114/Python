"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Digest Authorization page
"""

from selenium.webdriver.common.by import By


# todo - break function into separate script page object
# todo - verify being on page
# todo - right click box
# todo - dismiss alert box
# todo - dismiss popup box
# user and pass: admin

class DigestAuthPage:
    def __init__(self, driver):
        self.driver = driver

    digest_LinkText = (By.XPATH, "//a[text()='Digest Authentication']")



    def digestAuth_Link(self):
        return self.driver.find_element(*DigestAuthPage.digest_LinkText)


    """        
    driver.find_element(By.XPATH, "//a[text()='Digest Authentication']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """

