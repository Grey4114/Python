"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This class is used as a simple gateway to the conftest fixtures
"""


import pytest
import inspect
import logging

# todo - add more info to logs


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('D:\\GitHub\\Python\\Selenium\\the_internet_herokuapp_website\\reports\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)      # set to Debug to grab all logs
        return logger


