"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the main webpage and runs all of the connected pages test scripts
"""

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

from utilities import BaseClass

# class TestEndToEnd(BaseClass):

"""
    def __init__(self, driver):
        self.driver = driver
"""



driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(3)




"""
def test_AB():
    # todo - break function into separate script page object
    driver.find_element(By.XPATH, "//a[text()='A/B Testing']").click()
    # ab_text = driver.find_element_by_xpath("//h3[text()='A/B Test Control']").text
    # assert ("A/B Test" in ab_text)
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[text()='A/B Testing']").click()
    # ab_text = driver.find_element_by_xpath("//h3[text()='A/B Test Control']").text
    # assert ("A/B Test" in ab_text)
    time.sleep(2)
    driver.back()
    driver.refresh()
    time.sleep(2)


def test_AddRemoveElements():
    # todo - break function into separate script page object
    # todo - verify being on page
    driver.find_element(By.XPATH, "//a[text()='Add/Remove Elements']").click()
    time.sleep(2)

    # Click Add Element twice to add 2 delete buttons
    driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()
    driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()
    time.sleep(2)

    # Remove delete buttons
    delButtons = driver.find_elements(By.XPATH, "//div[@id='elements']/button[@class='added-manually']")
    time.sleep(2)

    for button in delButtons:
        button.click()
        time.sleep(1)

    driver.back()
    driver.refresh()
    time.sleep(2)


def test_BasicAuth():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - select cancel and verify
    # todo - Enter name, pass and accept, then verify
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


def test_BrokenImages():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Verify all 3 images
    driver.find_element(By.XPATH, "//a[text()='Broken Images']").click()
    time.sleep(2)
    driver.back()
    driver.refresh()
    time.sleep(2)



def test_ChallengingDOM():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Button 1 and verify
    # todo - Button 2 and verify
    # todo - Button 3 and verify
    # todo - Verify code change
    driver.find_element(By.XPATH, "//a[text()='Challenging DOM']").click()
    time.sleep(2)
    driver.back()
    driver.refresh()
    time.sleep(2)
    

def test_Checkboxes():
    # todo - break function into separate script page object
    # todo - verify being on page

    driver.find_element(By.XPATH, "//a[text()='Checkboxes']").click()
    checkBoxs = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    for box in checkBoxs:
        time.sleep(1)
        box.click()

    time.sleep(2)
    driver.back()
    driver.refresh()
    time.sleep(2)


def test_ContextMenu():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - right click box
    # todo - dismiss alert box
    # todo - dismiss popup box
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


def test_DigestAuth():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - right click box
    # todo - dismiss alert box
    # todo - dismiss popup box
    # user and pass: admin
    driver.find_element(By.XPATH, "//a[text()='Digest Authentication']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_DisappearingElements():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - check that the Gallery button vanishes and comes back
    driver.find_element(By.XPATH, "//a[text()='Disappearing Elements']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_DragDrop():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - check the drag and drop
    driver.find_element(By.XPATH, "//a[text()='Drag and Drop']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_Dropdown():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - check the drop downs
    driver.find_element(By.XPATH, "//a[text()='Dropdown']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    
    
def test_DynamicContent():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - the dynamic content
    driver.find_element(By.XPATH, "//a[text()='Dynamic Content']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    


def test_DynamicControls():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - the dynamic controls
    driver.find_element(By.XPATH, "//a[text()='Dynamic Controls']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_DynamicLoading():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - the dynamic loading
    driver.find_element(By.XPATH, "//a[text()='Dynamic Loading']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_EntryAd():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - the Entry Ad
    driver.find_element(By.XPATH, "//a[text()='Entry Ad']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_ExitIntent():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - the Exit Intent
    driver.find_element(By.XPATH, "//a[text()='Exit Intent']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_FileDownload():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - File Download
    driver.find_element(By.XPATH, "//a[text()='File Download']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    
    
def test_FileUpload():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - File Upload
    driver.find_element(By.XPATH, "//a[text()='File Upload']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_FloatingMenu():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Floating menu
    driver.find_element(By.XPATH, "//a[text()='Floating Menu']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_ForgotPassword():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - ForgotPassword
    driver.find_element(By.XPATH, "//a[text()='Forgot Password']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_FormAuth():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Form Authentication
    driver.find_element(By.XPATH, "//a[text()='Form Authentication']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_Frames():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Frames
    driver.find_element(By.XPATH, "//a[text()='Frames']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_Geolocation():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Geolocation
    driver.find_element(By.XPATH, "//a[text()='Geolocation']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_HorizontalSlider():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Horizontal Slider
    driver.find_element(By.XPATH, "//a[text()='Horizontal Slider']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_Hovers():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Hovers
    driver.find_element(By.XPATH, "//a[text()='Hovers']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_InfiniteScroll():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Infinite Scroll
    driver.find_element(By.XPATH, "//a[text()='Infinite Scroll']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_Inputs():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Inputs
    driver.find_element(By.XPATH, "//a[text()='Inputs']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_JQueryUIMenus():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - JQuery UI Menus
    driver.find_element(By.XPATH, "//a[text()='JQuery UI Menus']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_JavaScriptAlerts():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Java Script Alerts
    driver.find_element(By.XPATH, "//a[text()='JavaScript Alerts']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_JavaScript_OnloadEventError():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Java Script Onload Event Error
    driver.find_element(By.XPATH, "//a[text()='JavaScript onload event error']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_KeyPresses():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Key Presses
    driver.find_element(By.XPATH, "//a[text()='Key Presses']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_LargeDeepDOM():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Large & Deep DOM
    driver.find_element(By.XPATH, "//a[text()='Large & Deep DOM']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_MultipleWindows():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Multiple Windows
    driver.find_element(By.XPATH, "//a[text()='Multiple Windows']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_NestedFrames():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Nested Frames
    driver.find_element(By.XPATH, "//a[text()='Nested Frames']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_NotificationMessages():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Notification Messages
    driver.find_element(By.XPATH, "//a[text()='Notification Messages']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_RedirectLink():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Redirect Link
    driver.find_element(By.XPATH, "//a[text()='Redirect Link']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_SecureFileDownload():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Secure File Download
    driver.find_element(By.XPATH, "//a[text()='Secure File Download']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_ShadowDOM():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Shadow Dom
    driver.find_element(By.XPATH, "//a[text()='Shadow DOM']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_ShiftingContent():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Shifting Content
    driver.find_element(By.XPATH, "//a[text()='Shifting Content']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    
def test_SlowResources():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Slow Resources
    driver.find_element(By.XPATH, "//a[text()='Slow Resources']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)



def test_SortableDataTables():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Sortable Data Tables
    driver.find_element(By.XPATH, "//a[text()='Sortable Data Tables']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_StatusCodes():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Status Codes
    driver.find_element(By.XPATH, "//a[text()='Status Codes']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


def test_Typos():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Typos
    driver.find_element(By.XPATH, "//a[text()='Typos']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    

def test_WYSIWYG_Editor():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - WYSIWYG_Editor
    driver.find_element(By.XPATH, "//a[text()='WYSIWYG Editor']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)

"""

def test_CloseBrowserWindow():
    time.sleep(3)
    driver.close()  # Closes Browser window
