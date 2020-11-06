"""
Created: 11/5/202
Script Type: Selenium Practice Script
Notes:
    This script is a selenium practice script using Raul Shetty's practice web page.

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
radio_buttons = driver.find_elements_by_name("radioButton")     # Finds all of the radio button elements
radio_buttons[1].click()    # Clicks on the 2nd button













