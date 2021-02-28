"""
Website:
Date Created:
Notes:
"""

import pytest
from selenium import webdriver
import time
driver = None


# format below is from - https://docs.pytest.org/en/latest/example/simple.html
def pytest_addoption(parser):   # use to change browsers at launch
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose a browser, default is Chrome")


@pytest.fixture(scope="class")
def setup(request):     # add request to make driver object avialable in other scripts
    global driver   # makes the driver object a global

    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\msedgedriver.exe")

    driver.get("https://<website>")
    driver.maximize_window()

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
