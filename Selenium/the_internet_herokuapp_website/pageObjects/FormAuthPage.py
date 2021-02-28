"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    username: tomsmith
    password: SuperSecretPassword!
"""


from selenium.webdriver.common.by import By



class FormAuthPage:
    def __init__(self, driver):
        self.driver = driver

    form_Link = (By.XPATH, "//a[text()='Form Authentication']")         # Main Page link
    form_Header = (By.XPATH, "//h2[text()='Login Page']")               # Page header text

    form_User = (By.XPATH, "//input[@id='username']")                   # Username field
    form_Pass = (By.XPATH, "//input[@id='password']")                   # Password Field
    form_Login = (By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")        # Login button
    form_Valid = (By.XPATH, "//div[@class='flash success']")            # Valid flash message
    form_Invalid = (By.XPATH, "//div[@class='flash error']")            # Invalid flash message
    form_Logout = (By.XPATH, "//i[@class='icon-2x icon-signout']")      # Login button



    def formAuth_LinkText(self):
        return self.driver.find_element(*FormAuthPage.form_Link)

    def formAuth_HeaderText(self):
        return self.driver.find_element(*FormAuthPage.form_Header)

    def formAuth_Username(self):
        return self.driver.find_element(*FormAuthPage.form_User)

    def formAuth_Password(self):
        return self.driver.find_element(*FormAuthPage.form_Pass)

    def formAuth_LoginButton(self):
        return self.driver.find_element(*FormAuthPage.form_Login)

    def formAuth_ValidText(self):
        return self.driver.find_element(*FormAuthPage.form_Valid)

    def formAuth_InvalidText(self):
        return self.driver.find_element(*FormAuthPage.form_Invalid)

    def formAuth_LogoutButton(self):
        return self.driver.find_element(*FormAuthPage.form_Logout)

