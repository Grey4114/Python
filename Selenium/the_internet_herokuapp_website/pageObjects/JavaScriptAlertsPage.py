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

    javaAlert_LinkText = (By.XPATH, "//a[text()='JavaScript Alerts']")
    javaAlert_Header = (By.XPATH, "//h3[text()='JavaScript Alerts']")

    # todo - result text path
    javaAlert_Result = (By.XPATH, " ")


    # todo - alert button path
    alert_Button = (By.XPATH, " ")
    # todo - Alert OK path
    alert_Ok = (By.XPATH, " ")
    # todo - Alert text path
    alert_Text = (By.XPATH, " ")


    # todo - ConFirm button path
    confirm_Button = (By.XPATH, " ")
    # todo - confirm ok path
    confirm_Ok = (By.XPATH, " ")
    # todo - confirm cancel path
    confirm_Cancel = (By.XPATH, " ")
    # todo - confirm text path
    confirm_Text = (By.XPATH, " ")


    # todo - Promt field path
    prompt_Field = (By.XPATH, " ")
    # todo - Promt ok path
    prompt_Ok = (By.XPATH, " ")
    # todo - Prompt cancel path
    prompt_Cancel = (By.XPATH, " ")
    # todo - Prompt text path
    prompt_Text = (By.XPATH, " ")



    def javaScriptAlerts_Link(self):
        return self.driver.find_element(*JavaScriptAlertsPage.javaAlert_LinkText)

    def javaScriptAlerts_HeaderText(self):
        return self.driver.find_element(*JavaScriptAlertsPage.javaAlert_Header)

    def javaScriptAlerts_Results(self):
        return self.driver.find_element(*JavaScriptAlertsPage.javaAlert_Result)



    def javaScriptAlerts_AlertButton(self):
        return self.driver.find_element(*JavaScriptAlertsPage.alert_Button)

    def javaScriptAlerts_AlertOK(self):
        return self.driver.find_element(*JavaScriptAlertsPage.alert_Ok)

    def javaScriptAlerts_AlertText(self):
        return self.driver.find_element(*JavaScriptAlertsPage.alert_Text)


    def javaScriptAlerts_ConfirmButton(self):
        return self.driver.find_element(*JavaScriptAlertsPage.confirm_Button)

    def javaScriptAlerts_ConfirmOk(self):
        return self.driver.find_element(*JavaScriptAlertsPage.confirm_Ok)

    def javaScriptAlerts_ConfirmCancel(self):
        return self.driver.find_element(*JavaScriptAlertsPage.confirm_Cancel)

    def javaScriptAlerts_ConfirmText(self):
        return self.driver.find_element(*JavaScriptAlertsPage.confirm_Text)



    def javaScriptAlerts_PromptField(self):
        return self.driver.find_element(*JavaScriptAlertsPage.prompt_Field)

    def javaScriptAlerts_PromptOk(self):
        return self.driver.find_element(*JavaScriptAlertsPage.prompt_Ok)

    def javaScriptAlerts_PromptCancel(self):
        return self.driver.find_element(*JavaScriptAlertsPage.prompt_Cancel)

    def javaScriptAlerts_PromptText(self):
        return self.driver.find_element(*JavaScriptAlertsPage.prompt_Text)