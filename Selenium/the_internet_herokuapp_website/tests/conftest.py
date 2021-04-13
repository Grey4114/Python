"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    conftest.py script
"""
import os

import pytest
from selenium import webdriver
import time
driver = None


# use to change browsers at launch
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose a browser, default is Chrome")


@pytest.fixture(scope="class")
def setup(request):     # add request to make driver object avialable in other scripts
    global driver       # makes the driver object a global

    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")    # Starts the webpage maximized
        chrome_options.add_argument("--headless")  # Sets it so that the web page is not shown.
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)

    elif browser_name == "firefox":
        # Note: Setting from - https://www.programcreek.com/python/example/115596/selenium.webdriver.FirefoxOptions
        options = webdriver.FirefoxOptions()
        # options.set_preference("dom.webnotifications.serviceworker.enabled", False)
        # options.set_preference("dom.webnotifications.enabled", False)
        options.add_argument('--headless')
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
        driver.maximize_window()

    elif browser_name == "edge":
        # Note: Need to do more research for these settings
        driver = webdriver.Edge(executable_path="C:\\msedgedriver.exe")
        driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/")
    request.cls.driver = driver     # creates a class object called cls.driver for driver
    yield   # runs close last
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    # The next line changes the dir where to save the files
    os.chdir("D:/GitHub/Python/Selenium/the_internet_herokuapp_website/tests_screenShots")

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


