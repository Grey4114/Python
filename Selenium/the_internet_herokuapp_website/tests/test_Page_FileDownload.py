"""
Website:  https://the-internet.herokuapp.com/
Date:  2/9/2021
Notes:
    This script tests the XXX page
    ** Mae sure the C:/Users/chris_000/Downloads  directory is empty before running this script
"""
import os
import os.path
from os import path
import time
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.FileDownLoadPage import FileDownloadPage

class TestFileDownload(BaseClass):

    def test_file_download(self):
        # Enter the Page
        log = self.getLogger()
        fileDownload_page = FileDownloadPage(self.driver)
        log.info("TEST START")
        fileDownload_page.fileDownload_LinkText().click()


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/download"
        log.info("URL: " + url)


        # Verify the Header
        header_text = fileDownload_page.fileDownload_HeaderText().text
        assert ("File Downloader" in header_text)
        log.info("Header: " + header_text)


        # Find files and download
        count = 0
        filelist = fileDownload_page.fileDownload_FileList()
        for file in filelist:
            file.click()
            count += 1


        # Get a count of the files in the directory
        time.sleep(30)
        dir_list = os.listdir("C:/Users/chris_000/Downloads")
        num_files = len(dir_list)

        # Verify that the # of files in the dir = the # of downloaded files
        assert count == num_files

        # Todo - RAR files sometimes do not delete
        # Remove all of the downloaded files from the directory
        os.chdir("C:/Users/chris_000/Downloads")
        for f in dir_list:
            os.remove(f)
        log.info("Downloads: Passed")


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

