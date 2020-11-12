"""
Created: 11/5/202
Script Type: Selenium Practice Script
Notes:
    This script is a selenium practice script using Raul Shetty's practice web page.
    Install selenium
    Install and run Chrome Driver

Webpage used: https://rahulshettyacademy.com/AutomationPractice/
"""

# Selenium webdriver import
from selenium import webdriver

# Setting driver variable to the Chrome driver
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

# Maximizes the Chrome window
driver.maximize_window()

# Defining the webpage to be tested
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# RADIO BUTTONS
# Find the radio buttons and click the 2nd button
radio_buttons = driver.find_elements_by_name("radioButton")
radio_buttons[1].click()


# TODO - COUNTRY TEXT ENTRY FIELD
# Enter a the beginning of a country
text_field = driver.find_elements_by_name()


# TODO - DROPDOWN MENU
# Find the dropdown box and select option 2
# drop_down = driver.find_elements_by_name("dropdown-class-example")
# drop_down[1].click()



# TODO - CHECKBOX
# Find the checkbox and check all 3 options
check_box = driver.find_elements_by_name()

# TODO - SWITCH WINDOW
# Find the switch window and select
switch_window = driver.find_elements_by_name()

# TODO - SWITCH TABS
# Find the switch tabs and select
switch_tabs = driver.find_elements_by_name()

# TODO - SWITCH ALERTS
# Find the switch alerts, enter name and select
switch_alerts = driver.find_elements_by_name()


# TODO - DISPLAY ELEMENTS
# Find display elements and hide/show


# TODO - MOUSE HOVER OVER
# Find display hover and show









