"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script runs all of the connected pages test scripts
"""

import time
from utilities.BaseClass import BaseClass
from tests.test_Page_AB import TestPageAB
from tests.test_Page_AddRemoveElements import TestAddRemoveElements
from tests.test_Page_BasicAuth import TestBasicAuth
from tests.test_Page_BrokenImages import TestBrokenImages
from tests.test_Page_ChallengingDOM import TestChallengingDOM
from tests.test_Page_Checkboxes import TestCheckboxes
from tests.test_Page_ContextMenu import TestContextMenu
from tests.test_Page_DigestAuth import TestDigestAuth
from tests.test_Page_DisappearingElements import TestDisappearingElements
from tests.test_Page_DragDrop import TestDragDrop
from tests.test_Page_DropDown import TestDropdown
from tests.test_Page_DynamicContent import TestDynamicContent
from tests.test_Page_DynamicControls import TestDynamicControls
from tests.test_Page_DynamicLoading import TestDynamicLoading
from tests.test_Page_EntryAd import TestEntryAd
from tests.test_Page_ExitIntent import TestExitIntent
from tests.test_Page_FileDownload import TestFileDownload
from tests.test_Page_FileUpload import TestFileUpload
from tests.test_Page_FloatingMenu import TestFloatingMenu
from tests.test_Page_ForgotPassword import TestForgotPassword
from tests.test_Page_FormAuth import TestFormAuth
from tests.test_Page_Frames import TestFrames
from tests.test_Page_Geolocation import TestGeolocation
from tests.test_Page_HorizontalSlider import TestHorizontalSlider
from tests.test_Page_Hovers import TestHovers
from tests.test_Page_InfiniteScroll import TestInfiniteScroll
from tests.test_Page_Inputs import TestInputs
from tests.test_Page_JavaScriptAlerts import TestJavaScriptAlerts
from tests.test_Page_JavaScriptOnloadEventError import TestJavaScript_OnloadEventError
from tests.test_Page_JQueryUIMenus import TestJQueryUIMenus
from tests.test_Page_KeyPresses import TestKeyPresses
from tests.test_Page_LargeDeepDOM import TestLargeDeepDOM
from tests.test_Page_MultipleWindows import TestMultipleWindows
from tests.test_Page_NestedFrames import TestNestedFrames
from tests.test_Page_NotificationMessages import TestNotificationMessages
from tests.test_Page_RedirectLink import TestRedirectLink
from tests.test_Page_SecureFileDownload import TestSecureFileDownload
from tests.test_Page_ShadowDOM import TestShadowDOM
from tests.test_Page_ShiftingContent import TestShiftingContent
from tests.test_Page_SlowResources import TestSlowResources
from tests.test_Page_SortableDataTables import TestSortableDataTables
from tests.test_Page_StatusCodes import TestStatusCodes
from tests.test_Page_Typos import TestTypos
from tests.test_Page_WYSIWYG_Editor import TestWYSIWYG_Editor


class TestEndToEnd(BaseClass):
    def test_RunAll(self):
        TestPageAB()
        TestAddRemoveElements()
        TestBasicAuth()
        TestBrokenImages()
        TestChallengingDOM()
        TestCheckboxes()
        TestContextMenu()
        TestDigestAuth()
        TestDisappearingElements()
        TestDragDrop()
        TestDropdown()
        TestDynamicContent()
        TestDynamicControls()
        TestDynamicLoading()
        TestEntryAd()
        TestExitIntent()
        TestFileDownload()
        TestFileUpload()
        TestFloatingMenu()
        TestForgotPassword()
        TestFormAuth()
        TestFrames()
        TestGeolocation()
        TestHorizontalSlider()
        TestHovers()
        TestInfiniteScroll()
        TestInputs()
        TestJavaScriptAlerts()
        TestJavaScript_OnloadEventError()
        TestJQueryUIMenus()
        TestKeyPresses()
        TestLargeDeepDOM()
        TestMultipleWindows()
        TestNestedFrames()
        TestNotificationMessages()
        TestRedirectLink()
        TestSecureFileDownload()
        TestShadowDOM()
        TestShiftingContent()
        TestSlowResources()
        TestSortableDataTables()
        TestStatusCodes()
        TestTypos()
        TestWYSIWYG_Editor()
