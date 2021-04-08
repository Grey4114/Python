"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.NotificationMessagesPage import NotificationMessagesPage

class TestNotificationMessages(BaseClass):

    def test_notification_messages(self):
        # Enter the Page
        log = self.getLogger()
        notificationMessages_page = NotificationMessagesPage(self.driver)
        log.info("TEST START")
        notificationMessages_page.notificationMessages_LinkText().click()

        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/notification_message_rendered"
        log.info("URL: " + url)

        # Verify the Header
        header_text = notificationMessages_page.notificationMessages_HeaderText().text
        assert ("Notification Message" in header_text)
        log.info("Header: " + header_text)


        # Verify Notification Message
        first_msg = notificationMessages_page.notificationMessages_MessageText().text

        while True:
            notificationMessages_page.notificationMessages_ClickHere().click()
            next_msg = notificationMessages_page.notificationMessages_MessageText().text

            if first_msg != next_msg:
                # log.info(first_msg)
                # log.info(next_msg)
                break

        assert first_msg != next_msg


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



