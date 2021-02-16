"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - Frames


class FramesPage:
    def __init__(self, driver):
        self.driver = driver

    frames_LinkText = (By.XPATH, "//a[text()='Frames']")

    def frames_Link(self):
        return self.driver.find_element(*FramesPage.frames_LinkText)



    """
    driver.find_element(By.XPATH, "//a[text()='Frames']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """
