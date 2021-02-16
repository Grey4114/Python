"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - Shifting Content


class ShiftingContentPage:
    def __init__(self, driver):
        self.driver = driver

    shifting_LinkText = (By.XPATH, "//a[text()='Shifting Content']")

    def shiftingContent_Link(self):
        return self.driver.find_element(*ShiftingContentPage.shifting_LinkText)



    """    
    driver.find_element(By.XPATH, "//a[text()='Shifting Content']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """
