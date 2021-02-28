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

    notification_Link = (By.XPATH, "//a[text()='Notification Messages']")       # Main Page link
    notification_Header = (By.XPATH, "//h3[text()='Notification Message']")    # Page header text
    notification_Click = (By.XPATH, "//a[@href='/notification_message']")       # Click here link
    notification_Message = (By.ID, "flash")                                     # Alert Message


    def notificationMessages_LinkText(self):
        return self.driver.find_element(*NotificationMessagesPage.notification_Link)

    def notificationMessages_HeaderText(self):
        return self.driver.find_element(*NotificationMessagesPage.notification_Header)

    def notificationMessages_ClickHere(self):
        return self.driver.find_element(*NotificationMessagesPage.notification_Click)

    def notificationMessages_Message(self):
        return self.driver.find_element(*NotificationMessagesPage.notification_Message)


