"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the main webpage and runs all of the connected pages test scripts
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import BaseClass

# class TestPrimary(BaseClass):
# class TestPrimary:
"""
    def __init__(self, driver):
        self.driver = driver
"""

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(3)


def test_AB():
    # todo - break function into separate script page object
    driver.find_element(By.XPATH, "//a[text()='A/B Testing']").click()
    ab_text = driver.find_element_by_xpath("//h3[text()='A/B Test Control']").text
    assert ("A/B Test" in ab_text)
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[text()='A/B Testing']").click()
    ab_text = driver.find_element_by_xpath("//h3[text()='A/B Test Control']").text
    assert ("A/B Test" in ab_text)
    time.sleep(2)
    driver.back()
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
    time.sleep(2)


def test_BasicAuth():
    # todo - break function into separate script page object
    # todo - verify being on page
    # todo - Add 2 delete buttons and remove them
    "(user and pass: admin)"
    driver.find_element(By.XPATH, "//a[text()='Basic Auth']").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)


"""
"Broken Images"
driver.find_element_by_xpath("//a[text()='Broken Images']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Challenging DOM"
driver.find_element_by_xpath("//a[text()='Challenging DOM']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Checkboxes"
driver.find_element_by_xpath("//a[text()='Checkboxes']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Context Menu"
driver.find_element_by_xpath("//a[text()='Context Menu']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Digest Authentication(user and pass: admin)"
driver.find_element_by_xpath("//a[text()='Digest Authentication']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Disappearing Elements"
driver.find_element_by_xpath("//a[text()='Disappearing Elements']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Drag and Drop"
driver.find_element_by_xpath("//a[text()='Drag and Drop']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Dropdown"
driver.find_element_by_xpath("//a[text()='Dropdown']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Dynamic Content"
driver.find_element_by_xpath("//a[text()='Dynamic Content']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Dynamic Controls"
driver.find_element_by_xpath("//a[text()='Dynamic Controls']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Dynamic Loading"
driver.find_element_by_xpath("//a[text()='Dynamic Loading']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Entry Ad"
driver.find_element_by_xpath("//a[text()='Entry Ad']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Exit Intent"
driver.find_element_by_xpath("//a[text()='Exit Intent']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"File Download"
driver.find_element_by_xpath("//a[text()='File Download']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"File Upload"
driver.find_element_by_xpath("//a[text()='File Upload']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Floating Menu"
driver.find_element_by_xpath("//a[text()='Floating Menu']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Forgot Password"
driver.find_element_by_xpath("//a[text()='Forgot Password']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Form Authentication"
driver.find_element_by_xpath("//a[text()='Form Authentication']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Frames"
driver.find_element_by_xpath("//a[text()='Frames']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Geolocation"
driver.find_element_by_xpath("//a[text()='Geolocation']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Horizontal Slider"
driver.find_element_by_xpath("//a[text()='Horizontal Slider']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Hovers"
driver.find_element_by_xpath("//a[text()='Hovers']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Infinite Scroll"
driver.find_element_by_xpath("//a[text()='Infinite Scroll']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Inputs"
driver.find_element_by_xpath("//a[text()='Inputs']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"JQuery UI Menus"
driver.find_element_by_xpath("//a[text()='JQuery UI Menus']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"JavaScript Alerts"
driver.find_element_by_xpath("//a[text()='JavaScript Alerts']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"JavaScript onload event error"
driver.find_element_by_xpath("//a[text()='JavaScript onload event error']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Key Presses"
driver.find_element_by_xpath("//a[text()='Key Presses']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Large & Deep DOM"
driver.find_element_by_xpath("//a[text()='Large & Deep DOM']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Multiple Windows"
driver.find_element_by_xpath("//a[text()='Multiple Windows']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Nested Frames"
driver.find_element_by_xpath("//a[text()='Nested Frames']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Notification Messages"
driver.find_element_by_xpath("//a[text()='Notification Messages']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Redirect Link"
driver.find_element_by_xpath("//a[text()='Redirect Link']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Secure File Download"
driver.find_element_by_xpath("//a[text()='Secure File Download']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Shadow DOM"
driver.find_element_by_xpath("//a[text()='Shadow DOM']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Shifting Content"
driver.find_element_by_xpath("//a[text()='Shifting Content']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Slow Resources"
driver.find_element_by_xpath("//a[text()='Slow Resources']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Sortable Data Tables"
driver.find_element_by_xpath("//a[text()='Sortable Data Tables']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Status Codes"
driver.find_element_by_xpath("//a[text()='Status Codes']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"Typos"
driver.find_element_by_xpath("//a[text()='Typos']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"WYSIWYG Editor"
driver.find_element_by_xpath("//a[text()='WYSIWYG Editor']").click()
time.sleep(3)
driver.back()
time.sleep(3)

"""


def test_CloseBrowserWindow():
    time.sleep(3)
    driver.close()  # Closes Browser window
