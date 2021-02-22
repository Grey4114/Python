"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
"""

import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.ContextMenuPage import ContextMenuPage


# todo - verify right click box
# todo - verify dismiss alert box
# todo - verify dismiss popup box


class TestContextMenu(BaseClass):

    def test_contex_menu(self):
        # Enter the Page
        log = self.getLogger()
        contextmenu_page = ContextMenuPage(self.driver)
        log.info("TEST START")
        contextmenu_page.contextMenu_Link().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/context_menu"
        log.info("URL Passed: " + url)


        # Verify the Header
        header_text = contextmenu_page.contextMenu_HeaderText().text
        assert ("Contex Menu" in header_text)
        log.info("Header Passed: " + header_text)



        # Verify right click box
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Verify dismiss alert box
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")

        # Verify dismiss popup box
        # xxx_page.xxxx_Item().click()
        # xXxX = xxxx_page.xxxx_Elements()
        # assert (xXxX in xxxx)
        # log.info("Elements Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()


        """       
   
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

        """
