"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This class is used as a simple gateway to the conftest fixtures
"""


import pytest
import inspect
import logging

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# @pytest.mark.usefixtures("setup")
class BaseClass:

    """
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('D:\\GitHub\Various\\Selenium_Rahul_Course\\section_20\\reports\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)      # set to Debug to grab all logs
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))


    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
    """

