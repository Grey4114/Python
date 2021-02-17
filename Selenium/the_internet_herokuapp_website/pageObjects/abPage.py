"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the AB Testing page objects
"""

from selenium.webdriver.common.by import By

# todo - check title text

class abPage:
    def __init__(self, driver):
        self.driver = driver


    ab_LinkText = (By.XPATH, "//a[text()='A/B Testing']")   # Main Website link to page


    def ab_Link(self):
        return self.driver.find_element(*abPage.ab_LinkText)


    """        
    # ab_text = driver.find_element_by_xpath("//h3[text()='A/B Test Control']").text
    # assert ("A/B Test" in ab_text)
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[text()='A/B Testing']").click()
    # ab_text = driver.find_element_by_xpath("//h3[text()='A/B Test Control']").text
    # assert ("A/B Test" in ab_text)
    time.sleep(2)
    driver.back()
    driver.refresh()
    time.sleep(2)
    """


