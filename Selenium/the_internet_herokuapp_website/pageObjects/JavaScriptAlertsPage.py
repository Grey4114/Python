"""
Website:  https://the-internet.herokuapp.com/
Date:  2/15/2021
Notes:
    This script tests the Exit Intent page
"""


from selenium.webdriver.common.by import By

class JavaScriptAlertsPage:
    def __init__(self, driver):
        self.driver = driver

    javaAlert_Link = (By.XPATH, "//a[text()='JavaScript Alerts']")      # Main Page link
    javaAlert_Header = (By.XPATH, "//h3[text()='JavaScript Alerts']")       # Page header text
    javaAlert_Result = (By.ID, "result")                                # JS Alert Button
    alert_Button = (By.XPATH, "//button[@onclick='jsAlert()']")      # JS Alert button
    confirm_Button = (By.XPATH, "//button[@onclick='jsConfirm()']")        # ConFirm button
    prompt_Button = (By.XPATH, "//button[@onclick='jsPrompt()']")  # Promt button


    def javaScriptAlerts_LinkText(self):
        return self.driver.find_element(*JavaScriptAlertsPage.javaAlert_Link)

    def javaScriptAlerts_HeaderText(self):
        return self.driver.find_element(*JavaScriptAlertsPage.javaAlert_Header)

    def javaScriptAlerts_Results(self):
        return self.driver.find_element(*JavaScriptAlertsPage.javaAlert_Result)

    def javaScriptAlerts_AlertButton(self):
        return self.driver.find_element(*JavaScriptAlertsPage.alert_Button)

    def javaScriptAlerts_ConfirmButton(self):
        return self.driver.find_element(*JavaScriptAlertsPage.confirm_Button)

    def javaScriptAlerts_PromptButton(self):
        return self.driver.find_element(*JavaScriptAlertsPage.prompt_Button)

