"""
Website:  https://the-internet.herokuapp.com/
Date:  2/16/2021
Notes:
    This script tests the A/B Test page using the abPage objects script

"""

import time
import pytest
from utilities import BaseClass
from pageObjects import abPage


class TestAB(BaseClass):
    # todo - add page tests
    # todo - grab page header text
    # todo - assert header text or other text


    def test_one(self):
        log = self.getLogger()

        ab_page = abPage(self.driver)

        ab_page.ab_Link().click()

        


