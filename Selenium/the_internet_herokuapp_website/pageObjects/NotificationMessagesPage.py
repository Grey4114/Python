"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


# todo - break function into separate script page object
# todo - verify being on page
# todo - Notification Messages


class NotificationMessagesPage:
    def __init__(self, driver):
        self.driver = driver

    notification_LinkText = (By.XPATH, "//a[text()='Notification Messages']")

    def notificationMessages_Link(self):
        return self.driver.find_element(*NotificationMessagesPage.notification_LinkText)



    """
    driver.find_element(By.XPATH, "//a[text()='Notification Messages']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    """
