"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the main webpage and runs all of the connected pages test scripts
"""

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from tests import test_Page_AB


from utilities.BaseClass import BaseClass

class TestEndToEnd(BaseClass):
    def __init__(self, driver):
        self.driver = driver

        """ 
        test_Page_AB
        test_Page_AddRemoveElements
        
        test_Page_BasicAuth
        test_Page_BrokenImages
        
        test_Page_ChallengingDOM
        test_Page_Checkboxes
        test_Page_ContextMenu
        
        test_Page_DigestAuth
        test_Page_DisappearingElements
        test_Page_DragDrop
        test_Page_DropDown
        test_Page_DynamicContent
        test_Page_DynamicControls
        test_Page_DynamicLoading
        
        test_Page_EntryAd
        test_Page_ExitIntent
        
        test_Page_FileDownload
        test_Page_FileUpload
        test_Page_FloatingMenu
        test_Page_ForgotPassword
        test_Page_FormAuth
        test_Page_Frames
        
        test_Page_Geolocation
        
        test_Page_HorizontalSlider
        test_Page_Hovers
        
        test_Page_InfiniteScroll
        test_Page_Inputs
        
        test_Page_JavaScriptAlerts
        test_Page_JavaScriptOnloadEventError
        test_Page_JQueryUIMenus
        
        test_Page_KeyPresses
        
        test_Page_LargeDeepDOM
        
        test_Page_MultipleWindows
        
        test_Page_NestedFrames
        
        test_Page_NotificationMessages
        
        test_Page_RedirectLink
        
        test_Page_SecureFileDownload
        test_Page_ShadowDOM
        test_Page_ShiftingContent
        test_Page_SlowResources
        test_Page_SortableDataTables
        test_Page_StatusCodes
        
        test_Page_Typos
        
        test_Page_WYSIWYG_Editor
        """