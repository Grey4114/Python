"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - WYSIWYG_Editor



class WYSIWYGEditorPage:
    def __init__(self, driver):
        self.driver = driver

    wysiwyg_LinkText = (By.XPATH, "//a[text()='WYSIWYG Editor']")

    def WYSIWYGEditor_Link(self):
        return self.driver.find_element(*WYSIWYGEditorPage.wysiwyg_LinkText)


    """
    driver.find_element(By.XPATH, "//a[text()='WYSIWYG Editor']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """
