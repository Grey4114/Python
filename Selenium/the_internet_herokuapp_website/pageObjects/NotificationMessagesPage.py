"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By


class NotificationMessagesPage:
    def __init__(self, driver):
        self.driver = driver

    notification_LinkText = (By.XPATH, "//a[text()='Notification Messages']")
    notification_Header = (By.XPATH, "//h3[text()='Notification Messages']")

    # todo - click path
    notification_Click = (By.XPATH, " ")

    # todo - message path
    notification_Message = (By.XPATH, " ")



    def notificationMessages_Link(self):
        return self.driver.find_element(*NotificationMessagesPage.notification_LinkText)

    def notificationMessages_HeaderText(self):
        return self.driver.find_element(*NotificationMessagesPage.notification_Header)

    def notificationMessages_ClickHere(self):
        return self.driver.find_element(*NotificationMessagesPage.notification_Click)

    def notificationMessages_Message(self):
        return self.driver.find_element(*NotificationMessagesPage.notification_Message)


