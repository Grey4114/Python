"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    conftest.py script
"""

# import pytest
# from selenium import webdriver
# import time
# driver = None

"""
# use to change browsers at launch
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose a browser, default is Chrome")


@pytest.fixture(scope="class")
def setup(request):     # add request to make driver object avialable in other scripts
    global driver       # makes the driver object a global

    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")

    driver.get("https://the-internet.herokuapp.com/")
    driver.maximize_window()

    request.cls.driver = driver     # creates a class object called cls.driver for driver
    yield   # runs close last
    driver.close()
"""