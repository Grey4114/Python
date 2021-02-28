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


        # todo - Verify Notification Message
        time.sleep(3)
        count = 0


        while count > 2:
            notificationMessages_page.notificationMessages_ClickHere().click()
            message = notificationMessages_page.notificationMessages_Message().text
            log.info(message)


            """
            if "Action succesful" in message:
                if count > 1:
                    log.info("Action succesful")
                    count += 1

            elif "Action unsuccesful" in message:
                if count > 1:
                    log.info("Action unsuccesful, please try again")
                    count += 1
            else:
                log.info("no check")

            """



        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()



