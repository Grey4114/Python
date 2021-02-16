"""
Website:  https://the-internet.herokuapp.com/
Date:  2/14/2021
Notes:
    This script tests the ContextMenu page
"""

from selenium.webdriver.common.by import By


# todo - break function into separate script page object
# todo - verify being on page
# todo - right click box
# todo - dismiss alert box
# todo - dismiss popup box


class ContextMenuPage:
    def __init__(self, driver):
        self.driver = driver

    context_LinkText = (By.XPATH, "//a[text()='Context Menu']")


    def contextMenu_Link(self):
        return self.driver.find_element(*ContextMenuPage.context_LinkText)




    """       
    driver.find_element(By.XPATH, "//a[text()='Context Menu']").click()
    time.sleep(2)

    action = ActionChains(driver)
    action.context_click(driver.find_element(By.XPATH, "//div[@id='hot-spot']")).perform()

    # driver.find_element(By.XPATH, "//div[@id='hot-spot']").click()

    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()

    alert2 = driver.switch_to.alert
    time.sleep(1)
    alert2.send_keys(Keys.ESCAPE)
    time.sleep(1)


    driver.back()
    driver.refresh()
    time.sleep(3)
    
    """