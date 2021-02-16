"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the Basic Auth page
"""

from selenium.webdriver.common.by import By

# todo - break function into separate script page object
# todo - verify being on page
# todo - select cancel and verify
# todo - Enter name, pass and accept, then verify


class BasicAuthPage:
    def __init__(self, driver):
        self.driver = driver

    basic_LinkText = (By.XPATH, "//a[text()='Basic Auth']")


    def basicAuth_Link(self):
        return self.driver.find_element(*BasicAuthPage.basic_LinkText)



    """
    # user and pass: admin
    # validateText2 = "Confirm OK"
    driver.find_element(By.XPATH, "//a[text()='Basic Auth']").click()
    # time.sleep(2)
    alert = driver.switch_to.alert
    alert.authenticate('admin', 'admin')
    time.sleep(2)
    # alert.send_keys("admin")
    # alert.send_keys(Keys.TAB)
    # time.sleep(2)
    # alert.send_keys("admin")
    # alert.accept()
    # alert.dismiss()
    time.sleep(2)
    # confirmText = confirm.text  # assigns the text to an object
    # assert validateText2 in confirmText
    driver.back()
    driver.refresh()
    time.sleep(2)
    """

