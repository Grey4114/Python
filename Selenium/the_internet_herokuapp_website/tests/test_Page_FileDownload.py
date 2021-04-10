"""
Website:  https://the-internet.herokuapp.com/download
Created:  2/9/2021
Notes:
    Connected Page Object Script - /pageObjects/FileDownLoadPage.py

    ** All the files in the C:/Users/chris_000/Downloads directory will be deleted
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
        fileDownload_page.fileDownload_LinkText().click()


        # Verify the Header
        header_text = fileDownload_page.fileDownload_HeaderText().text
        assert ("File Downloader" in header_text)
        log.info("Header: " + header_text)


        # Verify the URL
        url = self.driver.current_url
        assert url == "https://the-internet.herokuapp.com/download"
        log.info("URL: " + url)


        # Verify - files downloaded
        filelist = fileDownload_page.fileDownload_FileList()
        for file in filelist:
            if ".txt" in file.text or ".png" in file.text:
                file.click()
                time.sleep(5)
                log.info(file.text)
                dir_list = os.listdir("C:/Users/chris_000/Downloads")
                assert file.text in dir_list


        # Remove all of the downloaded files from the directory
        dir_list = os.listdir("C:/Users/chris_000/Downloads")
        os.chdir("C:/Users/chris_000/Downloads")
        for f in dir_list:
            os.remove(f)


        # Exit the Page
        log.info(header_text + " - All Tests Passed")
        time.sleep(2)
        self.driver.back()
        self.driver.refresh()

